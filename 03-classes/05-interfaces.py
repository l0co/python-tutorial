#######################################################################################################################
print("interfaces are not implemented, but we have voodoo methods instead")

class MyIterable:
    def __init__(self):
        self.i = 0

    # iterable "interface"

    def __iter__(self):
        return self

    def __next__(self):
        self.i = self.i + 1
        if self.i == 10:
            raise StopIteration  # stop done by exception
                                 # by a pattern: when something expected and good happens, express this by exception
                                 # ¯\_(ツ)_/¯  why, God?
        return self.i

for i in MyIterable():
    print(i, end=" ")  # STDOUT: 1 2 3 4 5 6 7 8 9
print()

#######################################################################################################################
print("\neven a method can become iterator with 'yield' keyword")

def my_iterable():
    yield 1
    yield 2
    yield 3

for i in my_iterable():
    print(i, end=" ")  # STDOUT: 1 2 3
print()
print(my_iterable())  # STDOUT: <generator object my_iterable at 0x7fce03fac200>

#######################################################################################################################
print("\nthese generators can also be created with previously introduces 'for .. in' expressions")


my_generator = (i*i for i in range(10))
print(my_generator)  # STDOUT: <generator object <genexpr> at 0x7f2baef28270>
for i in my_generator:
    print(i, end=" ")  # STDOUT: 0 1 4 9 16 25 36 49 64 81


# TODOLF eq, hash for sets
