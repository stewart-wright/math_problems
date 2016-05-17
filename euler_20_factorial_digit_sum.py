import math_toolbox as mth

str_fact_one_hundred = str(mth.factorial(100))
total = 0

for digit in str_fact_one_hundred:
    total = total + int(digit)

print(total)