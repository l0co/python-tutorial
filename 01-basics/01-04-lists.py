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
    print(my_list)         # STDOUT: [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    my_list[2:3] = []
    print(my_list)

list_stdops()


