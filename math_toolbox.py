def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)

def factorise(number):
    factors = []
    for n in range(1,int(number+1/2)):
        if number % n == 0:
            factors.append(n)
    return factors