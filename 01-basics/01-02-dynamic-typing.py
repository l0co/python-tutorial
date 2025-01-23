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
    spam = "1"         # now here IDE at least complains with warning, but strict check is not enforced (next line)
    print(type(spam))  # STDOUT: <class 'str'>
type_hints()
