import sys

def sum_of_data(args):
    result = 0
    for arg in args:
        result = result + arg
    return result

def multiply(args):
    result = 1
    for arg in args:
        result = result * arg
    return result

def usage():
    print "Enter operator followed by at least two integers"
    print "Sign    Operation"
    print " +        Add"
    print " *       Multiply"
    exit(1)

def main():
    ops = None
    data = []
    ops_list = {
       "+" : sum_of_data,
       "*" : multiply
       }
    if len(sys.argv) < 3:
        usage()
    else:
        ops = sys.argv[1]
        for i in range(len(sys.argv) - 2):
            ele = sys.argv[i+2]
            if ele.isdigit():
                data.append(int(ele))
            else:
                print 'Please enter only integers'
                usage()
        if ops not in ops_list:
            usage()
        else:
            print ops_list.get(ops)(data)

if __name__ == '__main__':
    main()
        