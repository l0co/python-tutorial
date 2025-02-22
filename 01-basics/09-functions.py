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
print("\nfunction can have default and named arguments")
def default_args(a: int = 1, b: int = 2, c: int = 3):
    print(a + b + c)
default_args()  # STDOUT: 6
default_args(2)  # STDOUT: 7
default_args(c=10)  # STDOUT: 13

#######################################################################################################################
print("\nfunction can take multiple arguments as a tuple or a dict")
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

#######################################################################################################################
print("\ncollections can be unpacked to function arguments")
def unpack_arguments(a, b, c):
    print("a", a, "b", b, "c", c)
unpack_arguments(1, 2, 3)  # STDOUT: a 1 b 2 c 3
unpack_arguments(*[1, 2, 3])  # an equivalent, unpacks list
unpack_arguments(*(1, 2, 3))  # an equivalent, unpacks tuple
unpack_arguments(*{1, 2, 3})  # an equivalent, unpacks set
unpack_arguments(*{"a": 1, "b": 2, "c": 3})  # STDOUT: a a b b c c
                                             # surprise: unpacking a dict is only for people with XP>1500 and level>12
unpack_arguments(**{"a": 1, "b": 2, "c": 3})  # STDOUT: a 1 b 2 c 3
                                             # ¯\_(ツ)_/¯  why, God?

#######################################################################################################################
print("\nlambdas are single line only")
def lambda_test_1():
    my_lambda = lambda x, y: x + y
    print(my_lambda(1, 2))  # STDOUT: 3
lambda_test_1()

# however, this is a simple example to show, but it's not intended to be used like this (assigning as a variable)
def lambda_test_2():
    def transform_wisely(a: int, b: int, f: Callable[[int, int], int]):
        return f(a, b)
    print(transform_wisely(1, 5, lambda x, y: x + y))  # STDOUT: 6
lambda_test_2()

#######################################################################################################################
print("\nlamda keeps the surrounding scope")
def lambda_scope_test():
    lambdas = []
    for x in range(5):
        lambdas.append(lambda: x)
    for l in lambdas:
        print(l(), end=" ")  # STDOUT: 4 4 4 4 4
    print()

    lambdas = []
    for x in range(5):
        lambdas.append(lambda num=x: num)  # here's how to avoid this
    for l in lambdas:
        print(l(), end=" ")  # STDOUT: 0 1 2 3 4
    print()
lambda_scope_test()


