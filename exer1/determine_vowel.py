def determine_vowel():
    vowel_list = ('a','e','i','o','u')
    in_char = raw_input('Enter Character:')
    if in_char.lower() == 'bye':
        exit(0)
    if in_char.lower() in vowel_list:
        print '%s is a vowel' % in_char
    else:
        print '%s is not an vowel' % in_char

def main():
    print "Type 'bye' to exit"
    while True:
        determine_vowel()

if __name__ == "__main__":
    main()