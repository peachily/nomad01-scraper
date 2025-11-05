import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

def get_soup(url):
    print("fetching:", url)
    res = requests.get(url, headers=HEADERS)
    if res.status_code == 404:
        return None
    return BeautifulSoup(res.text, "html.parser")

def scrape_jobs(url):
    soup = get_soup(url)
    if soup is None:
        return []

    jobs = []
    job_list = soup.find_all("li", class_="bjs-jlid")

    for job in job_list:
        title = job.find("h4", class_="bjs-jlid__title")
        company = job.find("div", class_="bjs-jlid__company")
        desc = job.find("div", class_="bjs-jlid__description")
        link = job.find("a", href=True)

        job_data = {
            "title": title.text.strip() if title else "",
            "company": company.text.strip() if company else "",
            "description": desc.text.strip() if desc else "",
            "link": link["href"] if link else ""
        }
        jobs.append(job_data)

    return jobs

def scrape_engineering_all():
    all_jobs = []
    page = 1
    while True:
        url = f"https://berlinstartupjobs.com/engineering/page/{page}/"
        jobs = scrape_jobs(url)
        if not jobs:
            break
        all_jobs += jobs
        page += 1
    return all_jobs

def scrape_skill_area(skill):
    url = f"https://berlinstartupjobs.com/skill-areas/{skill}/"
    return scrape_jobs(url)

if __name__ == "__main__":
    skills = ["python", "typescript", "javascript"]

    print("\n=== Engineering jobs ===")
    engineering_jobs = scrape_engineering_all()
    print(f"총 {len(engineering_jobs)}개 수집 완료 \n")

    for skill in skills:
        print(f"=== {skill.capitalize()} jobs ===")
        skill_jobs = scrape_skill_area(skill)
        print(f"총 {len(skill_jobs)}개 수집 완료 \n")
