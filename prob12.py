import math

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
    num_factors = len(factors)
    for i in xrange(num_factors):
        factors.append(num/factors[i])
    return factors

def find_triangle_divisible(num_divisors):
    natural_num = 0
    found_divisors = 0
    while num_divisors > found_divisors:
        triangle_num = 0
        for i in xrange(1, natural_num+1):
            triangle_num += i
        natural_num += 1
        found_divisors = len(find_factors(triangle_num))

    return triangle_num
    
if __name__ == '__main__':
    print find_triangle_divisible(500)
