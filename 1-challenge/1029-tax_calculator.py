# 👇🏻 YOUR CODE 👇🏻:

def get_yearly_revenue(monthly_revenue):   # 연간 매출 계산: 월간매출을 인자로 받아서 연간 매출을 리턴하는 함수
  yearly_revenue = monthly_revenue * 12
  return yearly_revenue

def get_yearly_expenses(monthly_expenses):   # 연간 비용 계산: 월간비용을 인자로 받아서 연간 비용을 리턴하는 함수
  yearly_expenses = monthly_expenses * 12
  return yearly_expenses

def get_tax_amount(profit):   # 세금 계산: 이익을 인자로 받아서, 이익이 100,000보다 크면(if) 25% 세율을 적용하고, 크지 않으면(else) 15% 세율을 적용해서 세금금액을 리턴하는 함수
  if profit > 100000:
    tax_amount = profit * 25/100
  else:
    tax_amount = profit * 15/100
  return tax_amount

def apply_tax_credits(tax_amount, tax_credits):   # 세액 공제 적용: 세금금액. 세액공제율을 인자로 받아서, 공제할 금액을 리턴하는 함수
  final_tax_amount = tax_amount * tax_credits
  return final_tax_amount

# /YOUR CODE

# BLUEPRINT | DONT EDIT

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

# /BLUEPRINT