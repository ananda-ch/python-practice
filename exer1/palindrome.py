import re
import sys
import str_rev

def is_palindrome(arg):
    if arg == str_rev.reverse_string(arg):
        return True
    return False

def find_palindrome(arg):
    str_list = arg.split()
    op_dict = {}
    for strn in str_list:
        strn = re.sub('[^A-Za-z0-9]+', '', strn).lower()
        if is_palindrome(strn):
            if strn in op_dict:
                op_dict[strn] = int(op_dict.get(strn)) + 1
            else:
                op_dict[strn] = 1
    return op_dict

ip_str = sys.argv[1]
op_val = find_palindrome(ip_str)
print "String\tCount"
print '______\t_____'
for op in op_val:
    print '%s\t%s' % (op, op_val.get(op))