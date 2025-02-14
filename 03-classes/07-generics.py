#######################################################################################################################
print("generics are provided via typing module")

from typing import TypeVar, Generic

T = TypeVar('T')  # T and 'T' has to be the same, not yet covered by metaprogramming voodo


class MyGenericClass(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


int_instance = MyGenericClass[int](10)
print(int_instance.get_value())  # STDOUT: 10
str_instance = MyGenericClass[str]("Hello")
print(str_instance.get_value())  # STDOUT: Hello

#######################################################################################################################
print("bounded generics are possible, but doesn't work")

class Edible:
    pass

class Fruit(Edible):
    pass

class Stone:
    pass

E = TypeVar('E', bound=Edible)

class Eater(Generic[E]):
    def eat(self, e: E):
        print(f"eating {e}")

Eater().eat(Fruit())  # STDOUT: eating <__main__.Fruit object at 0x7fc4c7f0f820>
Eater().eat(Stone())  # STDOUT: eating <__main__.Stone object at 0x7f2d07933040>
