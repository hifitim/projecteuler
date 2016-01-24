if __name__ == "__main__":
    total = 0
    current = 2
    last = 1
    while current <= 4e6:
        if (current % 2 == 0):
            total += current
        temp = last
        last = current
        current += temp

    #solution: 4613732
    print "total:" + str(total)
