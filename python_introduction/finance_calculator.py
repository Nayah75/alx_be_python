monthly_income = int(input('Enter your monthly_income:'))
monthly_expenses = int(input('Enter your total monthly_expenses:'))
monthly_savings = monthly_income - monthly_expenses
print('Your monthly_savings are:', monthly_savings)
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print('Projected_savings after one year, with interest, is:', Projected_savings)

