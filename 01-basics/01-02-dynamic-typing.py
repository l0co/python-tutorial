#######################################################################################################################
print("dynamic typing: the same base flaw like in other scripting languages")
def dynamic_typing():
    spam = 1
    print(type(spam))  # STDOUT: <class 'int'>
    spam = "1"
    print(type(spam))  # STDOUT: <class 'str'>
dynamic_typing()

#######################################################################################################################
print("\nbut they know that and worked around already so Python TypeScript unlikely appears")
def type_hints():
    spam: int = 1
    print(type(spam))  # STDOUT: <class 'int'>
    spam = "1"         # now here IDE at least complaints with warning, but strict check is not enforced (next line)
    print(type(spam))  # STDOUT: <class 'str'>
type_hints()

#######################################################################################################################
print("\nand the biggest question here is why to reuse the same var with different type if we have a variable removal")
def remove_var():
    spam: int = 1
    print(spam)
    del spam
    # print(spam)  # ERROR: local variable 'spam' referenced before assignment
remove_var()

#######################################################################################################################
print("\nlets delve into the flaw a bit more")
def dynamic_typing_in_methods(a, b, c):
    # print(a + b // c)  # ALLOWED but ERROR: unsupported operand type(s) for //: 'int' and 'str'
    # print(a.my_property)  # ALLOWED but ERROR: 'int' object has no attribute 'my_property'
    # print(a[b])  # ALLOWED but ERROR: 'int' object is not subscriptable
    # ¯\_(ツ)_/¯  why, God?
    pass  # this is an empty code block
dynamic_typing_in_methods(1, 2, "three")

#######################################################################################################################
print("\nrecognizing development patterns")
# a - try with many different things, maybe you're lucky
# a - try to find some usages in other code, maybe you're lucky
# a - look on stackoverflow for examples, maybe you're lucky
# a - ask ChatGPT, he will know
# a - don't even try to look into docs because they don't bother to specify function argument types in docs
def make_money_for_me(a):
    if a == ["magic string", 123333, 0.2]:
        print("making a lot of money for you")
    else:
        raise Exception("If you don't know how to use it, just don't use it!")
make_money_for_me(["list", "maybe?"])

