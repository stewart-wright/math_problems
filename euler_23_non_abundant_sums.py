import math_toolbox as mth


def sum_factors(list_of_factors):
    total = 0
    for entry in list_of_factors:
        total = total + entry
    return total


def check_abundance(n):
    sum = sum_factors(mth.factorise(n))
    if sum > n:
        return True
    else:
        return False

# TODO: make list of abundants under n/2