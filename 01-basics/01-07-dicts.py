#######################################################################################################################
print("dicts are LinkdeHashMap<Object, Object>")
def dicts():
    my_dict = {"one": 1, "two": 2}
    print(my_dict)  # STDOUT: {'one': 1, 'two': 2}

    # adding and modyfing elements
    my_dict["one"] = 10
    my_dict[3] = "three"  # keys types can be different
    print(my_dict)  # STDOUT: {'one': 10, 'two': 2, 'three': 3}

    # removing elements
    del my_dict["one"]
    print(my_dict)  # STDOUT: {'two': 2, 3: 'three'}

    # is there an element in dict?
    print("one" in my_dict)  # STDOUT: False

    # list of keys
    print(list(my_dict))  # STDOUT: ['two', 3]
    # set of keys
    print(set(my_dict))  # STDOUT: {3, 'two'}

    # list of values
    print(my_dict.values())  # STDOUT: dict_values([2, 'three'])
    # this is iteable, then
    print(list(my_dict.values()))  # STDOUT: [2, 'three']
    print(set(my_dict.values()))  # STDOUT: {2, 'three'}
dicts()

#######################################################################################################################
print("\ntyped dicts")
def typed_dicts():
    from typing import Dict
    my_dict: Dict[str, int] = {"one": 1, "two": 2, 3: "three"}  # same old, same old
    print(my_dict)  # STDOUT: {'one': 1, 'two': 2, 3: 'three'}
typed_dicts()


# TODOLF 5.5
