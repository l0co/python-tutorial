#######################################################################################################################
print("annotation is a function returning a function taking a function as an argument and returning another function "
      "taking function arguments as arguments")

def repeat(num_times):
    def whatever(func):  # name here does not matter, but you have to figure it out
        def whatever2(*args, **kwargs):  # same here, but "return def" is only available only in future Python
            for _ in range(num_times):
                func(*args, **kwargs)
        return whatever2
    return whatever


@repeat(3)
def greet(name):
    print(f"Hello {name}", end=", ")

greet("Lukasz")  # STDOUT: Hello Lukasz, Hello Lukasz, Hello Lukasz,
