def find_ele_in_list(ele, arg):
    if ele in arg:
        return True
    return False

def main():
    list1 = [1, 9, 15, 27, 5]
    list2 = [4, 5, 34, 6]
    
    for ele in list1:
        overlap = find_ele_in_list(ele, list2)
        if overlap:
            print "Lists have common elements"
            break

if __name__ == "__main__":
    main()