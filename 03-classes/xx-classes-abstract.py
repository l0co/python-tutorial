# TODOLF not in tutorial

#######################################################################################################################
print("class can be derived from another class")

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass


class MyClass(MyAbstractClass):
    def my_abstract_method(self):
        return "Here is my implementation of the abstract method"


# my_abstract_object = MyAbstractClass()  # This will raise TypeError: Can't instantiate abstract class MyAbstractClass
my_object = MyClass()
print(my_object.my_abstract_method())  # This will output: "Here is my implementation of the abstract method"

