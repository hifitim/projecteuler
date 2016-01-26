import math

def pretty_print_matrix(mat):
    for i in xrange(len(mat[0])):
        print mat[i]

def check_pythagorean_triple(a, b, c):
    if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
        return True
    return False

def find_pythagorean_triplet(num):
    #c = [[0 for x in xrange(num)] for x in xrange(num)]
    for a in xrange(1, num/2):
        for b in xrange(1, num/2):
            #c[i-1][j-1] = math.pow(i, j)
            print "a: " + str(a)
            print "b: " + str(b)
            c = math.pow(a, b)
            if ((a + b + c) == num) and check_pythagorean_triple(a, b, c):
                return (a * b * c)

if __name__ == "__main__":
    print find_pythagorean_triplet(1000)
