import math

def isPrimeNum(num):
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2,num_sqrt+1):
        if num % i == 0:
            return False
    return True

def largestPrimeFactorLessThanSqrt(num):
    largest = 0
    num_sqrt = int(math.ceil(math.sqrt(num)))
    print "num: " + str(num)
    print "num_sqrt: " + str(num_sqrt)
    for i in xrange(2, num_sqrt+1):
        if num % i == 0:
            print "testing for prime: " + str(i)
            if isPrimeNum(i):
                print "prime: " + str(i)
                largest = i
    return largest

def largestPrimeFactor(num):
    largestLessThanSqrt = largestPrimeFactorLessThanSqrt(num)
    print "largestLessThanSqrt: " + str(largestLessThanSqrt)
    if (not isPrimeNum(largestLessThanSqrt)):
        return num/largestLessThanSqrt
    return largestLessThanSqrt

if __name__ == "__main__":
    print "largest prime factor: " + str(largestPrimeFactor(26))
    #print "largest prime factor: " + str(largestPrimeFactor(600851475143))
