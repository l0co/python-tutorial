#######################################################################################################################
print("int and float")
def int_and_float():
    print(type(1))  # <class 'int'>
    print(type(1.1))  # <class 'float'>
    print(5/2, type(5/2))  # 2.5 float (floating point integer division)
    print(5//2, type(5//2), 5 % 2, type(5 % 2))  # 2 int 1 int (integer division and modulo)
                                                 # funny, complaints about no spaces around modulo operator, but not
                                                 # about division operators
int_and_float()

#######################################################################################################################
print("\nstrings")
def strings():

    # quotes (no defined in code style)
    print('hello single quoted')  # hello single quoted
    print("hello double quoted")  # hello double-quoted

    # special chars
    print("hello\nnew line")  # hello
                              # new line
    print(r"hello\nraw string")  # hello\nraw string

    # multiline
    print("""hello
    new line""")  # hello
                  #           newline
                  # so \n at the end of each line is preserved
    print("""hello\
    same line""")  # hello    same line
                  # to skip \n use "\" at the end of line
                  # but sill, "new line" is indented as in the code, this can be overcome with textwrap.dedent()
    print("hello "
          "same line")  # hello same line
                        # better multiline strings - auto concatenation with no operator
    print("hello " +
          "same line")  # hello same line
                        # the same with "+" operator

    # multiplication
    print(3 * "hello ")  # hello hello hello

    # finding chars, substrings etc. (nice!)
    my_string = "0123456789"
    print(my_string[0])      # 0 - first char
    print(my_string[-1])     # -1 - last char
    print(my_string[2:5])    # 234 - substring (from the head)
    print(my_string[2:])     # 23456789 - substring (from the head)
    print(my_string[-3:-1])  # 78 - substring (from the tail)
    print(my_string[-3:])    # 789 - substring (from the tail)
    print(my_string[5:2])    # watch out: empty string with no additional warning (!)
    # print(my_string[52])   # but this ends up with "string index out of range" exception
    # my_string[0] = "1"     # and finally, strings are immutable
                             # so ""'str' object does not support item assignment" exception is thrown here

    # length
    print(len(my_string))  # by built-in multipurpose function
strings()
