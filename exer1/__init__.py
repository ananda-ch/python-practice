def max_of_three(var1, var2, var3):
    max = var1
    if var2 > max:
        max = var2
    if var3 > max:
        max = var3
    return max

max_of_three(10,5,29)