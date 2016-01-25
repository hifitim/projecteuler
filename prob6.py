import math

def sum_of_squares(lo, hi):
    sum = 0
    for i in xrange(lo, hi+1):
        sum += math.pow(i, 2)
    return sum

def square_of_sum(lo, hi):
    sum = 0
    for i in xrange(lo, hi+1):
        sum += i
    sum = math.pow(sum, 2)
    return sum

if __name__ == "__main__":
    print "difference: " + str(math.fabs(sum_of_squares(1, 100) - square_of_sum(1,100)))
