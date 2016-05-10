import str_length
import sys

def find_longest_word(arg):
    max_length = 0
    long_word = None
    for word in arg:
        str_len = str_length.find_str_len(word)
        if str_len > max_length:
            max_length = str_len
            long_word = word
    return long_word, max_length

def main():
    if len(sys.argv) < 2:
        print 'Enter atleast one word'
        exit(1)
    data = []
    for i in range(len(sys.argv) - 1):
        data.append(sys.argv[i+1])
    
    long_word, length = find_longest_word(data)
    print 'Longest word is %s with length %s ' % (long_word, length)

if __name__ == "__main__":
    main()