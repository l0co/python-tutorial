#######################################################################################################################
print("@Value classes (Java records) are creatable using built-in Lombok")

from dataclasses import dataclass

@dataclass
class ValueObject:
    first_name: str
    last_name: str

# a constructor is created implicitely
# valueObject: ValueObject = ValueObject()  # ERROR: __init__() missing 2 required positional arguments:
                                            # 'first_name' and 'last_name'

valueObject: ValueObject = ValueObject("John", "Rambo")
print(valueObject)  # STDOUT: ValueObject(first_name='John', last_name='Rambo')
# so they even have toString() ........... (°o°)

# is a value class really a value class?
valueObject.first_name = "Jane"
print(valueObject)  # STDOUT: ValueObject(first_name='Jane', last_name='Rambo')
# no, but anyway a huge achievement goes here

# last but not least, for @dataclass the "field declared in a class is a static one" contract is broken
# print(ValueObject.first_name)  # ERROR: type object 'ValueObject' has no attribute 'first_name'


