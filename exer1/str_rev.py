import sys

def reverse_string(arg):
    result = ''
    for s in range(len(arg)):
        result = result + arg[len(arg) - (s + 1)]
    return result

str_input = sys.argv[1]
print reverse_string(str_input)