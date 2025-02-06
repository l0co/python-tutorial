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
    # CAUTION: Python allows "no brackets" notation which can be really, really misleading, like
    #          if I call function(x, y, z), are "x, y, z" arguments or one tuple argument?

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

# after what we've seen, now a bit of conclusion comes, it's about the tutorial ad: Python’s elegant syntax
# the example is from the sources I've seen during these tests:
#
# class map(Iterator[_S], Generic[_S]):
#     @overload
#     def __init__(self, __func: Callable[[_T1], _S], __iter1: Iterable[_T1]) -> None: ...
#     @overload
#     def __init__(self, __func: Callable[[_T1, _T2], _S], __iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> None: ...
#     @overload
#     def __init__(
#         self, __func: Callable[[_T1, _T2, _T3], _S], __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]
#     ) -> None: ...
#     @overload
#     def __init__(
#         self,
#         __func: Callable[[_T1, _T2, _T3, _T4], _S],
#         __iter1: Iterable[_T1],
#         __iter2: Iterable[_T2],
#         __iter3: Iterable[_T3],
#         __iter4: Iterable[_T4],
#     ) -> None: ...
#     @overload
#     def __init__(
#         self,
#         __func: Callable[[_T1, _T2, _T3, _T4, _T5], _S],
#         __iter1: Iterable[_T1],
#         __iter2: Iterable[_T2],
#         __iter3: Iterable[_T3],
#         __iter4: Iterable[_T4],
#         __iter5: Iterable[_T5],
#     ) -> None: ...
#
# ¯\_(ツ)_/¯  why, God?

