from sys import stdout

def collatz_sequence_length(start_num):
    num_terms = 1
    current_num = start_num
    while current_num > 1:
        if current_num % 2 == 0:
            current_num /= 2
        else:
            current_num = (current_num * 3) + 1
        num_terms += 1
    return num_terms

def find_longest_collatz_seq(end_num):
    longest_seq = 0
    loc = 0
    for i in xrange(1, long(end_num)+1):
        if ((i/end_num)*1000) % 1 == 0:
            stdout.write("\r\t\t\t\t")
            stdout.flush()
            stdout.write("\r%s%% \t %d/%d" % (str((i/end_num)*100), i, end_num))
        temp_len = collatz_sequence_length(i)
        if temp_len > longest_seq:
            longest_seq = temp_len
            loc = i
    print ""
    return loc

if __name__ == '__main__':
    print find_longest_collatz_seq(1e6)
