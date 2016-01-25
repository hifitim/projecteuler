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

#works, super slow
def evenly_divisible(lo, hi):
    num = 1
    while True:
        if num % 5e6 == 0:
            print num
        divisible = True
        for i in xrange(lo, hi+1):
            if num % i != 0:
                divisible = False
                break
        if divisible:
            break
        num += 1
    return num

def evenly_divisible2(lo, hi):
    factors = []
    for i in xrange(lo, hi):
        factors += find_factors(i)
        if is_prime_num(i):
            factors.append(i)

    new_factors = []
    for i in xrange(lo, hi):
        print "i: " + str(i)
        for j in new_factors:
            if i % j == 0:
                i /= j
        for j in factors:
            if i % j == 0:
                print "adding: " + str(j)
                new_factors.append(j)
                i /= j
        if i != 1:
            print "adding leftover: " + str(i)
            new_factors.append(i)

    print new_factors
    total_product = 1
    for i in new_factors: total_product *= i
    return total_product

if __name__ == "__main__":
    print evenly_divisible2(1, 20)
