import sys

def find_str_len(arg):
    cnt = 0
    for ch in arg:
        cnt = cnt + 1
    return cnt

def main():
    ip_str = sys.argv[1]
    print 'Input string length : %s' % find_str_len(ip_str)

if __name__ == "__main__":
    main()