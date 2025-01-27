#######################################################################################################################
print("standard 'if'")
def standard_if(x: int):  # for all those who are scared about "dynamic typing" examples, type hints DO work for
                          # functions so you might try to write a consistent code in Python as well
    if x == 1:
        print("one")
    elif x == 2:
        print("two")
    else:
        print("more than two")
# standard_if()  #  ERROR: standard_if() missing 1 required positional argument
                 # leaving this example to point out that this is an INTERPRETED language
                 # this means that they go each line one after another and try to execute it
                 # if there's an error, you'll only know that in the runtime
                 # so, calling a function with one argument, with no arguments at all is "permitted"
standard_if(1)  # STDOUT: one
standard_if(2)  # STDOUT: two
standard_if(3)  # STDOUT: more than two

#######################################################################################################################
print("\nstandard 'while'")
def standard_while(x: int):
    while x < 10:
        print("inc; ", end="")  # "end" argument is an end line char, default is "\n" but one can overwrite
        x = x + 1
    else:
        print("x reached 10")
standard_while(5)  # STDOUT: inc; inc; inc; inc; inc; x reached 10

#######################################################################################################################
print("\n'for' is 'in something' by default")
def for_in():
    for x in [0, 1, 2]:  # in list
        print(x, end="")  # STDOUT: 012
    print("")

    for x in range(0, 2):  # in range
        print(x, end="")  # STDOUT: 01 (first inclusive, last exclusive)
    print("")

    for x in range(0, 9, 3):  # in range with custom step (3)
        print(x, end="")  # STDOUT: 036
    print("")

    print(range(0, 2).__iter__())  # STDOUT: <range_iterator object at 0x7f5f5053b900>
                                   # is range a list? not - all arguments passed to "for" should implement
                                   # "iterable" pattern, but in Python's way:
    from collections.abc import Iterable
    print(isinstance(range(0, 2), Iterable))  # STDOUT: True
    print(isinstance([0, 1, 2], Iterable))  # STDOUT: True
for_in()

#######################################################################################################################
print("\nstandard 'break' and 'continue'")
def break_continue():
    for x in range(1, 100):  # A-loop
        print("x=", x, end=" ", sep="")
        for y in range(1, 100):  # B-loop
            print("y=", y, end=" ", sep="")
            break  # breaks B-loop
        if x % 2 == 0:
            break  # breaks A-loop
    print("")
    # STDOUT: x=1 y=1 x=2 y=1 
    # but no label-based break, though

    for x in range(1, 10):
        if x % 2 == 0:
            continue
        print("x=", x, end=" ", sep="")
    # STDOUT: x=1 x=3 x=5 x=7 x=9

    # same for while
    print("")
    x = 0
    while x < 5:
        x = x + 1
        if x % 2 == 0:
            continue
        print("x=", x, end=" ", sep="")
        if x % 3 == 0:
            break
   # STDOUT: x=1 x=3
break_continue()

#######################################################################################################################
print("\nloops + 'else'")
def loop_else():
    for x in range(0, 1):
        pass  # STDOUT: does nothing
    else:
        print("for/while loop has 'else' block which is executed only if loop hasn't been broken")
    for x in range(0, 1):
        break
    else:
        print("for/while loop has 'else' block which is not executed if loop has been broken")
loop_else()  # STDOUT: for/while loop has 'else' block which is executed only if loop hasn't been broken

#######################################################################################################################
# print("\nstandard 'switch' which is 'match'")
# def switch_match(http_code: int):
#     match http_code:
#         case 404:
#             return "Not found"
#         case _:
#             return "In my professional opinion, something has fucked up"
# switch_match(500)  # STDOUT: In my professional opinion, something has fucked up
# wow, I'm commenting out this since they figured out this clause in 2021, and I still have python 3.8 :)
