#######################################################################################################################
print("dynamic typing - a base flaw like in other scripting languages")
def dynamic_typing():
    spam = 1
    print(type(spam))  # <class 'int'>
    spam = "1"
    print(type(spam))  # <class 'str'>
dynamic_typing()

#######################################################################################################################
print("\nbut they know that and worked around already so Python TypeScript unlikely appears")
def type_hints():
    spam: int = 1
    print(type(spam))  # <class 'int'>
    spam = "1"         # now here it complains with warning, but still works (look at the next line)
    print(type(spam))  # <class 'str'>
type_hints()
