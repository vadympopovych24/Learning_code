import decimal


monthly_income = decimal.Decimal(input('Input your monthly income: '))
income_tax = decimal.Decimal('0.18')
military_tax = decimal.Decimal('0.015')

all_tax = str(monthly_income * (income_tax + military_tax))

print('Amount of taxes that must be paid: ' + all_tax) 