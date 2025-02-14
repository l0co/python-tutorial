#######################################################################################################################
print("interfaces are not implemented, but we have vodoo methods instead")

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
    print(i)  # STDOUT: 0 .. 9
