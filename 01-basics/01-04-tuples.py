#######################################################################################################################
print("tuple is a predefined number of items of given type in a row")
def tuple_basics():
    # no direct equivalent in Java language and reflected by different implementations (org.apache.commons.lang3.tuple)
    my_tuple = 1, 2, "three"
    print(my_tuple)  # STDOUT: (1, 2, 'three')
    print(type(my_tuple))  # STDOUT: <class 'tuple'>

    my_tuple_2 = (1, 2, "three")
    print(my_tuple_2)  # STDOUT: (1, 2, 'three')
    # so, tuple should really be surrounded with () and it's the same
    # CAUTION: Python allows "no brackets" notation which can be really, but really misleading, like
    #          if I call function(x, y, z), are "x, y, z" arguments or one tuple argument?
    #          WARN: if it's a tuple, it can't be parametrized (look at the examples below)

    # tuples are immutable
    # my_tuple[0] = 1  # ERROR: 'tuple' object does not support item assignment

    empty = ()  # empty tuple is created this way
    print(type(empty))  # STDOUT: <class 'tuple'>
    empty_2: tuple = ()  # while this a proper way :)

    one_element_tuple = ("one")  # so, now let's try to create one element tuple according to other rules
    print(type(one_element_tuple))  # STDOUT: <class 'str'>
                                    # ¯\_(ツ)_/¯  why, God?
                                    # God: don't ask

    one_element_tuple_2 = ("one",)  # one element tuple approach 2, looks like the proper way
    print(type(one_element_tuple_2))  # STDOUT: <class 'tuple'>

    one_element_tuple_3 = "one",  # one element tuple approach 3
    print(type(one_element_tuple_3))  # STDOUT: <class 'tuple'>

    # some final thoughts
    # if you look for something super-weird like lines ended with comma, bracket expressions ended with comma
    # probably function arguments ended with comma ... and stuff: Python is for you
    # like endless lists created with [1, 2, :)]
tuple_basics()

#######################################################################################################################
print("\nso, can we at least make a tuple 'typed'?")
def typed_tuple():
    my_tuple: tuple = (1, 2, "three")
    print(my_tuple)  # STDOUT: (1, 2, 'three')
    my_tuple = ("one", "two", 3)
    print(my_tuple)  # STDOUT: ('one', 'two', 3)
    # so, not directly

    my_tuple_2: tuple[int, int, str] = (1, 2, "three")  # maybe this? feel not, because it warns
                                                        # WARN: Builtin 'tuple' cannot be parameterized directly
    print(my_tuple_2)  # STDOUT: (1, 2, 'three')
    my_tuple_2 = ("one", "two", 3)  # WARN: Expected type 'Tuple[int, int, str]', got 'Tuple[str, str, int]' instead
                                    # WOOOOW :O
    print(my_tuple_2)  # STDOUT: ('one', 'two', 3)
                       # but it works anyway

    # but here comes the big brother of tuple called Tuple
    # ¯\_(ツ)_/¯  why, God?
    from typing import Tuple
    my_big_brother_tuple: Tuple[str, int] = ("Alice", 25)  # does not complain that
                                                           # Builtin 'tuple' cannot be parameterized directly
                                                           # a big hope
    print(my_big_brother_tuple)  # STDOUT: ('Alice', 25)
    print(type(my_big_brother_tuple))  # <class 'tuple'>
    # now the big check comes
    my_big_brother_tuple = (25, "Alice")  # WARN: Expected type 'Tuple[str, int]', got 'Tuple[int, str]' instead
                                          # (but still works)
    print(my_big_brother_tuple)  # STDOUT: (25, 'Alice')
    print(type(my_big_brother_tuple))  # <class 'tuple'>

    # a kind of recap:
    # 1) tuple is not really typed, can warn you, but allows to do anything then
    # 2) a solution for that is Tuple, which is not really typed, can warn you, but allows to do anything then
    # ¯\_(ツ)_/¯  why, God?
    # ----> I'm anxiously waiting for TuplE in Python 4, it should be improved <----
typed_tuple()
