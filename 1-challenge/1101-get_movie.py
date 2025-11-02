# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

for movie_id in movie_ids:
  url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    title = data.get("title")   # get[title]
    overview = data.get("overview")
    vote_average = data.get("vote_average")

    print(f"제목: {title}")
    print(f"평점: {vote_average}")
    print(f"줄거리: {overview}\n")
  else:
    print(f"ID {movie_id}의 정보를 불러오지 못했습니다.")

# /YOUR CODE