#######################################################################################################################
print("class is a class")

class MyHellower:
    hello_count: int = 1  # everything is public by default

    def __init__(self, hello_count: int = 1):  # constructor and methods get the first "self" argument which is "this"
        self.hello_count = hello_count  # so in class methods you will be keeping repeat "self." for thousands times
                                        # ¯\_(ツ)_/¯  why, God?

    def hello(self, who: str):
        for i in range(self.hello_count):
            print(f"{self} says hello to {who} for {i+1} time")

    def create_dynamic_hello_count(self):
        self.dynamic_hello_count = 78

myHellower: MyHellower = MyHellower(2)  # instantiation with no "new"
myHellower.hello("Lukasz")  # STDOUT: <__main__.MyHellower object at 0x7ff4cc7887c0> says hello to Lukasz for 1 time
                            # STDOUT: <__main__.MyHellower object at 0x7ff4cc7887c0> says hello to Lukasz for 2 time
print(MyHellower)  # STDOUT: <class '__main__.MyHellower'> (class of type MyHellower?)
print(type(MyHellower))  # STDOUT: <class 'type'> (just a class?)
print(myHellower)  # STDOUT: <__main__.MyHellower object at 0x7f22790997c0> (object instance of MyHellower)

# make sure my field is an instance field
myHellower2 = MyHellower(3)
print(myHellower2.hello_count)  # STDOUT: 3
print(myHellower.hello_count)  # STDOUT: 2

# and here surprise comes
print(MyHellower.hello_count)  # STDOUT: 1
# so, declaring field at class level it makes it static class field
# which I then shadowed in a constructor
# so, by default instance fields shouldn't be mentioned on class, but in a constructor
# plus you can create a field ad-hoc in a method:
# print(myHellower.dynamic_hello_count)  # ERROR: 'MyHellower' object has no attribute 'dynamic_hello_count'
myHellower.create_dynamic_hello_count()
print(myHellower.dynamic_hello_count)  # STDOUT: 78

# a recap: Python is not only constructed about the concept "you don't know what is this variable type"
# but also introduces a concept: "you don't know what are this class fields"
