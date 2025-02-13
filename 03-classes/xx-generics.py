# TODOLF not in tutorial

from typing import TypeVar, Generic


T = TypeVar('T')


class MyGenericClass(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


# Teraz możemy używać MyGenericClass z określonym typem:
int_instance = MyGenericClass[int](10)
str_instance = MyGenericClass[str]("Hello")

print(int_instance.get_value())  # 10
print(str_instance.get_value())  # Hello
