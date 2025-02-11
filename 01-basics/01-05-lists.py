#######################################################################################################################
print("lists are defined with [] and there are no additional arrays")
def simple_list():
    print([1, 2, 3, 4])  # STDOUT: [1, 2, 3, 4]
    print(["list", 0, "of", 1, "different", 2, "item", 3, "types"])  # STDOUT: ['list', 0, 'of', 1, 'different', 2, 'item', 3, 'types']
simple_list()

#######################################################################################################################
print("\nsame accessing and slicing as strings")
def list_access_and_slicing():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list[0])      # STDOUT: 0 (first item)
    print(my_list[-1])     # STDOUT: 9 (last item)
    print(my_list[2:5])    # STDOUT: [2, 3, 4] (list slice: from the head)
    print(my_list[2:])     # STDOUT: [2, 3, 4, 5, 6, 7, 8, 9] (list slice: from the head)
    print(my_list[-3:-1])  # STDOUT: [7, 8] (list slice: from the tail)
    print(my_list[-3:])    # STDOUT: [7, 8, 9] (list slice: from the tail)
    print(my_list[5:2])    # CAUTION: empty list with no additional warning
    # print(my_list[52])   # ERROR: but this ends up with "list index out of range" exception
    my_list[0] = 100       # lists are mutable
    my_list[-1] = 200      # very are mutable
    print(my_list)         # STDOUT: [100, 1, 2, 3, 4, 5, 6, 7, 8, 200]
list_access_and_slicing()

#######################################################################################################################
print("\nthere are some standard operations supported")
def list_stdops():
    my_list = [0, 1, 2, 3, 4] + [5, 6, 7, 8, 9]  # concatenation
    print(my_list)  # STDOUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list.append(100)  # appending elements
    print(my_list)  # STDOUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
    my_list.remove(2)  # element removal
    print(my_list)  # [0, 1, 3, 4, 5, 6, 7, 8, 9, 100]

    def does_it_remove_all_the_same_elements():
        my_nested_list = [0, 1, 2, 2, 2, 5, 6, 7, 8, 9]
        my_nested_list.remove(2)
        print(my_nested_list)  # [0, 1, 2, 2, 5, 6, 7, 8, 9]
                               # so not, only the first one encountered
    does_it_remove_all_the_same_elements()
list_stdops()

#######################################################################################################################
print("\nlist elements removals and replacements")
def list_removals():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    del my_list[0]  # remove element with index 0 - first way
    print(my_list)  # STDOUT: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list.pop(0)  # remove element with index 0 - second way
    print(my_list)  # STDOUT: [2, 3, 4, 5, 6, 7, 8, 9]
    my_list[0:1] = []  # remove element with index 0 - third way (replace list slice with an empty list)
    print(my_list)  # STDOUT: [3, 4, 5, 6, 7, 8, 9]
    my_list[3:6] = []  #       0  1  2  3--4--5..6 (first element inclusive, last exclusive)
    print(my_list)  # STDOUT: [3, 4, 5, 9]
list_removals()

#######################################################################################################################
print("\nother list operations")
def list_ops():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list.append(10)  # append to the end
    print(my_list)  # STDOUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_list.extend(range(11, 15))  # extend list by iterable
    print(my_list)  # STDOUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    index_2 = my_list.index(2)  # give me the first index of element with value 2
    print(index_2)  # STDOUT: 2

    count_2 = my_list.count(2)  # count how many elements with value 2 is on the list
    print(count_2)  # STDOUT: 1

    my_list.sort(reverse=True)  # sort the list
    print(my_list)  # STDOUT: [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    my_list.reverse()  # reverses the list
    print(my_list)  # STDOUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    my_list_2 = my_list.copy()  # shallow list copy
    my_list.remove(0)
    my_list_2.remove(1)
    print(my_list)  # STDOUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(my_list_2)  # STDOUT: [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list_ops()

#######################################################################################################################
print("\nmaster len function")
def master_len():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(len(my_list))  # STDOUT: 10
master_len()


#######################################################################################################################
print("\nlist as a stack")
def list_as_stack():
    my_stack = [0, 1, 2]
    my_stack.append(3)
    my_stack.append(4)
    print(my_stack)  # STDOUT: [0, 1, 2, 3, 4]
    print(my_stack.pop())  # STDOUT: 4
    print(my_stack.pop())  # STDOUT: 3
    print(my_stack)  # STDOUT: [0, 1, 2]
list_as_stack()

#######################################################################################################################
print("\nlist as a LinkedList (LIFO, FIFO)")
def list_as_linkedlist():
    # a small comment to this:
    # appending to the end of a list and popping from the end of the list from the above example is efficient,
    # but it operates on a list tail, while the same operations on a list head are inneficient because
    # they would require to reallocate the whole list [O(n)]
    # so, Python provides a "deque wrapper" for lists which works in a very similar way to Java LinkedList
    # use it to implement FIFO and LIFO queues; but be aware, they differ in implementation details:
    # - Java LinkedList add/remove to/from whatever position: O(1)
    # - Python deque: add/remove to/from tail or head: O(1), to/from whatever position: unsupported
    # the implementation below is a circular queue: https://www.youtube.com/watch?v=CXmg8MRGv_k
    from collections import deque  # Python naming standard for classes is CamelCase for classes and snake_case for
                                   # functions and variables
                                   # ¯\_(ツ)_/¯  why, God?
                                   # but "deque" is a class which does not follow this standard
                                   # ¯\_(ツ)_/¯  why, God?
    my_list = [0, 1, 2]
    my_deque = deque(my_list)
    print(my_list)  # STDOUT: [0, 1, 2]
    print(my_deque)  # STDOUT: deque([0, 1, 2])
    my_deque.appendleft(-1)
    print(my_list)  # STDOUT: [0, 1, 2]
    print(my_deque)  # STDOUT: deque([-1, 0, 1, 2])
                     # CONCLUSION: deque creates a list copy
    print(my_deque.popleft())  # STDOUT: -1
    print(my_list)  # STDOUT: [0, 1, 2]
    print(my_deque)  # STDOUT: deque([0, 1, 2])
                     # CONCLUSION: deque toString (and possibly iterator) works as supposed
list_as_linkedlist()

#######################################################################################################################
print("\nlist mapping")
def list_mapping():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    mapped = map(lambda x: x**2, my_list)  # map class is iterable, takes the lambda and another iterable and produce
                                           # own iterable with lambda transformation
    print(list(mapped))  # STDOUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
                         # list can be created from iterable and shows the lambda transformation results
list_mapping()

#######################################################################################################################
print("\nlist comprehension")
def list_comprehension():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_square_list = [x ** 2 for x in my_list]  # a list can be created from other iterable with this expression
                                                # it stands for "call each item from 'my_list' x and for each do x**2"
    print(my_square_list)  # STDOUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    my_even_square_list = [x**2 for x in my_list if x % 2 == 0]  # additional 'if' clause can act a list filter
    print(my_even_square_list)  # STDOUT: [0, 4, 16, 36, 64]

    my_even_and_divisible_by_three_list = [x**2 for x in my_list if x % 2 == 0 if x % 3 == 0]  # more 'if'-s possible
                                                                                               # like it was no 'and' :O
    print(my_even_and_divisible_by_three_list)  # STDOUT: [0, 36]

    my_tuple_list = [(x, y) for x in [1, 2] for y in [3, 4]]  # tuple list can be cross-joined from many lists
    print(my_tuple_list)  # STDOUT: [(1, 3), (1, 4), (2, 3), (2, 4)]
list_comprehension()

#######################################################################################################################
print("\nnested list comprehension")
def nested_list_comprehension():
    my_vec_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    my_vec_list_flattened = [num for vec in my_vec_list for num in vec]
    print(my_vec_list_flattened)  # STDOUT: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for each vec in my_vec_list take num in vec and produce num
    # it's like...
    # curly braces show the inner expression meaning: [num {for vec in my_vec_list} for num in vec]
    # curly braces show the outer expression meaning: [{num} for vec in my_vec_list {for num in vec}]
    # equivalent of:
    my_vec_list_flattened = []
    for vec in my_vec_list:
        for num in vec:
            my_vec_list_flattened.append(num)
    print(my_vec_list_flattened)  # STDOUT: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_vec_list_flattened_2 = [[vec[i] for vec in my_vec_list] for i in range(3)]
    print(my_vec_list_flattened_2)  # STDOUT: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # inner and outer expresion is well separated here
    # equivalent of:
    my_vec_list_flattened_2 = []
    for i in range(3):
        my_vec_list_flattened_2.append([vec[i] for vec in my_vec_list])
    print(my_vec_list_flattened_2)  # STDOUT: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # because:
    print([vec[0] for vec in my_vec_list])
nested_list_comprehension()  # STDOUT: [1, 4, 7]

#######################################################################################################################
print("\ndel and lists")
def del_and_lists():
    my_list = [0, 1, "two", 3, 4, 5, 6, 7, 8, 9]
    del my_list[2]  # del removes the element by index (not by value)
    print(my_list)  # STDOUT: [0, 1, 3, 4, 5, 6, 7, 8, 9]
    del my_list[5:7]  # works with ranges too
    print(my_list)  # STDOUT: [0, 1, 3, 4, 5, 8, 9]
del_and_lists()
