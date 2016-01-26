import math

def find_pythagorean_triplet(num):    
    for a in xrange(1, num):
        for b in xrange(1, num):
            c = math.sqrt((a**2) + (b**2))
            if (a + b + c) == num:
                return (a * b * c)

if __name__ == "__main__":
    print find_pythagorean_triplet(1000)
