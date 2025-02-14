#######################################################################################################################
print("abstract is not implemented on language level, but provided by Lombok")

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):  # in future releases of Python they are gonna rename this ABC base class to :)
    @abstractmethod
    def my_abstract_method(self):
        pass


class MyClass(MyAbstractClass):
    def my_abstract_method(self):
        return 1

# my_object = MyAbstractClass()  # ERROR: Can't instantiate abstract class MyAbstractClass
                                 # with abstract methods my_abstract_method
my_object = MyClass()
print(my_object.my_abstract_method())  # STDOUT: 1

