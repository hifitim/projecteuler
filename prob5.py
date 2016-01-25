import math

def is_prime_num(num):
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2,num_sqrt+1):
        if num % i == 0:
            return False
    return True

def factors_less_than_sqrt(num):
    largest = 0
    factors = []
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2, num_sqrt+1):
        if num % i == 0:
            factors.append(i)
    return factors

def find_factors(num):
    factors = factors_less_than_sqrt(num)
    for i in xrange(len(factors)):
        factors.append(num/factors[i])
    return factors

def evenly_divisible(lo, hi):
    #first, find all factors for every number in the range
    factors = []
    for i in xrange(lo, hi):
        factors += find_factors(i)
        if is_prime_num(i):
            factors.append(i)
        #remove all the ones, since they multiply out to just one
        factors = [x for x in factors if x != 1]

    #the core logic is that you have to be able to make each of the numbers
    #in the range by multiplyihg two or more numbers in a list of factors.
    #if you can do that, you've found the minimum terms that can be multiplied
    #to make the final product
    new_factors = []
    for i in xrange(lo, hi):
        for j in new_factors:
            if i % j == 0:
                i /= j
        for j in factors:
            if i % j == 0:
                new_factors.append(j)
                i /= j
        if i != 1:
            new_factors.append(i)

    total_product = 1
    for i in new_factors: total_product *= i
    return total_product

if __name__ == "__main__":
    print evenly_divisible(1, 20)
