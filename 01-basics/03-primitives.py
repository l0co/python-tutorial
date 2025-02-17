#######################################################################################################################
print("int and float")
def int_and_float():
    print(type(1))  # STDOUT: <class 'int'>
    print(type(1.1))  # STDOUT: <class 'float'>
    print(5 / 2, type(5 / 2))  # STDOUT: 2.5 <class 'float'> (floating point integer division)
    print(5 // 2, type(5 // 2), 5 % 2, type(5 % 2))  # STDOUT: 2 <class 'int'> 1 <class 'int'> (int division and modulo)
int_and_float()

#######################################################################################################################
print("\nstrings")
def strings():

    # quotes (not s[ecified by code style)
    print('hello single quoted')  # STDOUT: hello single quoted
    print("hello double quoted")  # STDOUT: hello double-quoted

    # special chars
    print("hello\nnew line")  # STDOUT: hello
                              # new line
    print(r"hello\nraw string")  # STDOUT: hello\nraw string

    # multiline
    print("""hello
    new line""")  # STDOUT: hello
                  #           newline
                  # so \n at the end of each line is preserved
    print("""hello\
    same line""")  # STDOUT: hello    same line
                   # to skip \n use "\" at the end of line
                   # but still, "same line" part is indented as in the code, this can be overcome with textwrap.dedent()
    print("hello "
          "same line")  # STDOUT: hello same line (better multiline strings - auto concatenation with no operator)
    print("hello " +
          "same line")  # STDOUT: hello same line (the same with "+" operator)

    # multiplication
    print(3 * "hello ")  # STDOUT: hello hello hello

    # finding chars, substrings etc. (nice)
    my_string = "0123456789"
    print(my_string[0])      # STDOUT: 0 (first char)
    print(my_string[-1])     # STDOUT: 9 (last char)
    print(my_string[2:5])    # STDOUT: 234 (substring: from the head)
    print(my_string[2:])     # STDOUT: 23456789 (substring: from the head)
    print(my_string[-3:-1])  # STDOUT: 78 (substring: from the tail)
    print(my_string[-3:])    # STDOUT: 789 (substring: from the tail)
    print(my_string[5:2])    # CAUTION: empty string with no additional warning
    # print(my_string[52])   # ERROR: but this ends up with "string index out of range" exception
    # my_string[0] = "1"     # ERROR: 'str' object does not support item assignment" exception is thrown here
                             # so, finally, strings are immutable

    # checking whether a substring exists in string
    print("3" in my_string)  # STDOUT: True
    print("34" in my_string)  # STDOUT: True

    # length
    print(len(my_string))  # STDOUT: 10 (by built-in multipurpose function)
strings()

#######################################################################################################################
print("\nstrings comparison: Python implements iterable objects comparision")
def strings_comparison():
    # for all iterables we can use comparison, which compares 1st element, in case it differs returns,
    # in case it's equals takes another one
    print('A' < 'B')  # STDOUT: True
    print('B' < 'A')  # STDOUT: False
    print('AA' < 'AB')  # STDOUT: True
strings_comparison()

# TODOLF None and Optional
