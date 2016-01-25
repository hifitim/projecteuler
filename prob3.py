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

def largest_prime_factor(num):
    factors = factors_less_than_sqrt(num)
    prime_factors = []
    for i in xrange(len(factors)):
        new_factor = num/factors[i]
        if is_prime_num(new_factor):
            prime_factors.append(new_factor)
        if is_prime_num(factors[i]):
            prime_factors.append(factors[i])

    if len(prime_factors) > 0:
        return prime_factors[len(prime_factors)-1]
    else:
        return -1

if __name__ == "__main__":
    print "largest prime factor: " + str(largest_prime_factor(600851475143))
