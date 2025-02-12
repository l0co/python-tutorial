#######################################################################################################################
print("function definition")
def add2(x: int) -> int:  # takes int and returns int
    return x + 2
print(add2(5))  # STDOUT: 7

#######################################################################################################################
print("\nfunction can be stored as variable")
add2ref = add2
print(add2ref)  # STDOUT: <function add2 at 0x7ff44ab93b80>
print(type(add2ref))  # STDOUT: <class 'function'>
print(add2ref(5))  # STDOUT: 7

#######################################################################################################################
print("\nfunction can be represented as callable interface")
from typing import Callable  # already known
def consume_add_2(f: Callable[[int], int]):
                              # ^     ^
                              # |     |- return type
                              # |------- argument types
    # result = f("5")  # complaints about "str" type (as an argument type)
    # result: str = f(5)  # complaints about "str" type (as a return type)
    result: int = f(5)  # all types are proper, no complaints
    print(result)
consume_add_2(add2ref)  # STDOUT: 7
consume_add_2(add2)  # STDOUT: 7

#######################################################################################################################
print("\ndefault function arguments")
def default_args(a: int = 1, b: int = 2, c: int = 3):
    print(a + b + c)
default_args()  # STDOUT: 6
default_args(2)  # STDOUT: 7
default_args(c=10)  # STDOUT: 13

#######################################################################################################################
print("\nmultiple function arguments")
def multiple_args_1(*tuple_arg):  # provided as a tuple
    print(tuple_arg)
multiple_args_1(1, 2, 3)  # STDOUT: (1, 2, 3)

def multiple_args_2(**dict_arg):  # provided as a dict
    print(dict_arg)
multiple_args_2(one=1, two=2, three=3)  # STDOUT: {'one': 1, 'two': 2, 'three': 3}
# multiple_args_2(1, 2, 3)  # ERROR: multiple_args_2() takes 0 positional arguments but 3 were given

def multiple_args_3(*tuple_arg, **dict_arg):  # provided as a tuple and dict
    print(tuple_arg)  # STDOUT: (1, 2, 3)
    print(dict_arg)  # STDOUT: {'one': 1, 'two': 2, 'three': 3}
multiple_args_3(1, 2, 3, one=1, two=2, three=3)

# TODOLF 4.9.3
# TODOLF 4.9.4
# TODOLF 4.9.5
# TODOLF 4.9.6
# TODOLF 4.9.7
# TODOLF 4.9.8
# TODOLF 4.10
