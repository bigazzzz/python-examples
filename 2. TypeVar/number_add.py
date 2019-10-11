import decimal # десятичные числа

price = 4.7
count = 3
print(price*count) # 14.100000000000001 ???????
price = decimal.Decimal("4.7")
print(price*count) # 14.1 !!!!

import fractions # дробные числа

x = fractions.Fraction(3,7)
y = fractions.Fraction(3,6)
print(x,y) # 3/7 1/2
print(x+y) # 13/14
print(x+1) # 10/7
