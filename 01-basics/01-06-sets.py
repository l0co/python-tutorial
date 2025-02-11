#######################################################################################################################
print("sets are LinkedHashSet<Object>")
def sets():
    my_set = {1, 2, 2, 3}
    print(my_set)  # STDOUT: {1, 2, 3}

    # checking element is in set
    print(1 in my_set)  # STDOUT: True

    # set operations
    my_other_set = {2, 3, 3, 4}
    # sub
    print(my_set - my_other_set)  # STDOUT: {1}
    # sum
    print(my_set | my_other_set)  # STDOUT: {1, 2, 3, 4}
    # common part
    print(my_set & my_other_set)  # STDOUT: {2, 3}
    # distinct part
    print(my_set ^ my_other_set)  # STDOUT: {1, 4}
sets()

#######################################################################################################################
print("\ntyped sets")
def typed_sets():
    from typing import Set
    my_set: Set[int] = {1, 2, "three"}  # we already know that
    print(my_set)  # STDOUT: {1, 2, 'three'}
typed_sets()

#######################################################################################################################
print("\nsets can be created from iterables")
def set_iterables():
    my_set = set(range(4))  # set can be created from iterable with set()
    print(my_set)  # STDOUT: {0, 1, 2, 3}
    my_set = set("abracadabra")  # string is iterable too, even a list :)
    print(my_set)  # STDOUT: {'a', 'c', 'r', 'd', 'b'}
set_iterables()

#######################################################################################################################
print("\nset comprehension")
def set_comprehension():
    my_set = {x ** 2 for x in range(4)}  # same as for lists
    print(my_set)  # STDOUT: {0, 1, 4, 9}
set_comprehension()

#######################################################################################################################
print("\nsets comparison (NEITHER the same as string NOR other iterables)")
def sets_comparison():
    print({"A"} < {"B"})  # STDOUT: False
    print({"B"} < {"A"})  # STDOUT: False
    print({"AA"} < {"AB"})  # STDOUT: False
    print({"A", "A"} < {"A", "B"})  # STDOUT: True
    # and wait for it
    # .
    # .
    # .
    # for sets they compare number of elements
    # so if you have some collection on hand (of unknown type, because types are not very supported here
    # and top what you can expect is that you have "some" iterable collection)
    # comparison like this can blow up in your face
sets_comparison()
