#######################################################################################################################
print("'with' is a 'resource try ... catch' with autocloseable")

class MyManagedObject(object):
    def __enter__(self):  # achieved by voodoo methods
        print("starting")
        return self  # this object is used in 'with' clause

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("stopping")
        if exc_type is not None:
            print(f"exception: {exc_type}, {exc_val}")
            return True  # suppress exception


with MyManagedObject() as obj:
    print(f"working with: {obj}")
# STDOUT:
# starting
# working with: <__main__.MyManagedObject object at 0x7f930c0ee7c0>
# stopping

print()

with MyManagedObject() as obj:
    raise ValueError
# STDOUT:
# starting
# stopping
# exception: <class 'ValueError'>,
