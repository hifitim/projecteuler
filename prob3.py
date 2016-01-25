import math

def isPrimeNum(num):
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2,num_sqrt):
        if num % i == 0:
            return False
    return True

def factorsLessThanSqrt(num):
    largest = 0
    factors = []
    num_sqrt = int(math.ceil(math.sqrt(num)))
    for i in xrange(2, num_sqrt):
        if num % i == 0:
            factors.append(i)
    return factors

def largestPrimeFactor(num):
    factors = factorsLessThanSqrt(num)
    primeFactors = []
    for i in xrange(len(factors)):
        newFactor = num/factors[i]
        if isPrimeNum(newFactor):
            primeFactors.append(newFactor)
        if isPrimeNum(factors[i]):
            primeFactors.append(factors[i])

    if len(primeFactors) > 0:
        return primeFactors[len(primeFactors)-1]
    else:
        return -1

if __name__ == "__main__":
    #print "largest prime factor: " + str(largestPrimeFactor(600851475143))
    print "largest prime factor: " + str(largestPrimeFactor(12568441))
