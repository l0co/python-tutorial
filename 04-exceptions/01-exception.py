#######################################################################################################################
print("exception is a class")

# no voodoo this time:
print(ValueError)  # STDOUT: <class 'ValueError'>

#######################################################################################################################
print("\nexceptions can be thrown as a class")

try:  # try
    raise ValueError  # this exception is thrown as a class reference
except ValueError as e:  # catch
    print(f"exception: {e}")  # STDOUT: exception:
    print(type(e))  # STDOUT: <class 'ValueError'>
    print(e.args)  # STDOUT: ()
                   # (just prooving this is an object)
finally:  # finally
    print("ufff..")  # STDOUT: ufff..

#######################################################################################################################
print("\nexceptions can be thrown as an object")

try:
    raise ValueError(1, 2, 3)  # this exception is thrown as an instantiated object
except Exception as e:  # catch all
    print(f"exception: {e}")  # STDOUT: exception: (1, 2, 3)
    print(type(e))  # STDOUT: <class 'ValueError'>
    print(e.args)  # STDOUT: (1, 2, 3)

#######################################################################################################################
print("\ntry catch has else block which executed only when no exception was thrown")
# but, I don't see value it this, in java this is just a continuation of try{} block

try:
    print(1)  # STDOUT: 1
except Exception as e:
    print(2)  # not executed
else:
    print(3)  # STDOUT: 3

try:
    raise ValueError(1, 2, 3)
except ValueError as e:
    print(2)  # STDOUT: 2
else:
    print(3)  # not executed

#######################################################################################################################
print("\none can create own exceptions")

class PythonLanguageInconsistencyException(Exception):
    pass

try:
    raise PythonLanguageInconsistencyException()
except PythonLanguageInconsistencyException:
    print("an inconsistency detected in Python language")  # STDOUT: an inconsistency detected in Python language

