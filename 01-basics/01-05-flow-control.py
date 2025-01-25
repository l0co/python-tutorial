#######################################################################################################################
print("standard if")
def standard_if(x: int):  # for all those who are scared about "dynamic typing" examples, type hints DOES work for
                          # functions so you might try to write a consistent code in Python as well
    if x == 1:
        print("one")
    elif x == 2:
        print("two")
    else:
        print("more than two")
# standard_if()  #  ERROR: standard_if() missing 1 required positional argument
                 # leaving this example to point out that this is an INTERPETED language
                 # this means that they go each line one after another and try to execute it
                 # if there's an error, you'll only know that in the runtime
                 # so, calling a function with one argument, with no arguments at all is "permitted"
standard_if(1)  # STDOUT: one
standard_if(2)  # STDOUT: two
standard_if(3)  # STDOUT: more than two
