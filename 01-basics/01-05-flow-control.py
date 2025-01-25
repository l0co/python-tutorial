#######################################################################################################################
print("standard if")
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
print("\nstandard while")
def standard_while(x: int):
    while x < 10:
        print("inc; ", end="")  # "end" argument is an end line char, default is "\n" but one can overwrite
        x = x + 1
    else:
        print("x reached 10")
standard_while(5)  # STDOUT: inc; inc; inc; inc; inc; x reached 10

#######################################################################################################################
print("\nfor is \"in something\" by default")
def for_in():
    for x in [0, 1, 2]:  # in list
        print(x, end="")  # STDOUT: 012
    print("")
    for x in range(0, 2):  # in range
        print(x, end="")  # STDOUT: 01 (first inclusive, last exclusive)
    print("")
    for x in range(0, 9, 3):  # in range with custom step (3)
        print(x, end="")  # STDOUT: 036
for_in()


