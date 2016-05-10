def max_of_three(arg1, arg2, arg3):
    maximum = arg1
    if maximum < arg2:
        maximum = arg2
    if maximum < arg3:
        maximum = arg3
    print maximum

max_of_three(10, 5, 29)