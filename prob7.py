import math

def is_prime_num(num):
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2,num_sqrt+1):
        if num % i == 0:
            return False
    return True

def find_prime(num):
    prime_idx = 1
    current_num = 1
    while prime_idx < num:
        current_num += 1
        if is_prime_num(current_num):
            prime_idx += 1
    return current_num

if __name__ == "__main__":
    print "prime: " + str(find_prime(10001))
