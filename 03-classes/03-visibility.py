#######################################################################################################################
print("everything is public, but we pretend '_' variables aren't")

class MyProtectedFieldsStorage:
    def __init__(self):
        self._protected_value = 1

# this is why we pretend
print(MyProtectedFieldsStorage()._protected_value)  # STDOUT: 1

#######################################################################################################################
print("\nbut we can even better pretend we have private declarations with '__' variables")

class MyPrivateFieldsStorage:
    def __init__(self):
        self.__private_value = 2

# this is why this pretence is better
# print(MyPrivateFieldsStorage().__private_value)  # ERROR: 'MyPrivateFieldsStorage' object has no attribute
                                                   #        '__private_value'

# to achieve this a "name mangling" technique is used, it's as simple as
# 1. Python connects to a SOAP web service on python.org reporting a new class with a new private field
# 2. The global storage on python.org produces a new entry for the reported name
# 3. A name hash is calculated
# 4. Then this hash is passed back to the compiler
# 5. Instead of original name, python uses this hash as a variable name

# disclaimer: this will only be implemented in Python 6, curently it's:
print(MyPrivateFieldsStorage()._MyPrivateFieldsStorage__private_value)  # STDOUT: 2

