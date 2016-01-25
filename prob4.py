def is_palindrome(num):
    num_str = str(num)
    num_length = len(str(num))
    for i in xrange(num_length):
        if num_str[i] == num_str[num_length - 1 -i]:
            continue
        else:
            return False
    return True

def find_largest_palindrome_product(lo, hi):
    largest_palindrome_factor = -1

    for i in xrange(lo, hi):
        for j in xrange(lo , hi):
            product = i * j
            if (is_palindrome(product)) and (product > largest_palindrome_factor):
                largest_palindrome_factor = product

    for i in xrange(hi, lo):
        for j in xrange(lo, hi):
            product = i * j
            if (is_palindrome(product)) and (product > largest_palindrome_factor):
                largest_palindrome_factor = product

    return largest_palindrome_factor

if __name__ == "__main__":
    print "largest palindrome product: " + str(find_largest_palindrome_product(100, 1000))
