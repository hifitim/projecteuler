import math

def is_prime_num(num):
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2,num_sqrt+1):
        if num % i == 0:
            return False
    return True

def find_prime_sum_below(num):
    total = long(0)
    for i in xrange(long(num)):
        if is_prime_num(i):
            total += i
    return total

if __name__ == '__main__':
    print find_prime_sum_below(2e6)
