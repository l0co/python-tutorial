#######################################################################################################################
print("so, the code block is a tab indent, bye {}")
def function():
    print("hello from code block")
function()  # STDOUT: hello from code block

#######################################################################################################################
print("\nno local code block scope, and can't be easily worked around")
if True:
    local_scope_var_1 = 10
print(local_scope_var_1)  # CAUTION, STDOUT: 10
# CONCLUSION: it looks as a truly misleading inconsistency in relation to other langs because not always
# an inner code block creates a scope; sometimes it creates and sometimes not
# only function, class, etc. creates a local scope, but it's a function, class, etc...
def local_scope_test():
    local_scope_var_2 = 10
# print(local_scope_var_2)  # ERROR: local_scope_var_2 is not defined

#######################################################################################################################
print("\nshadowing vars")
global_scope_var = 1
def shadow_vars_1():
    print(global_scope_var)  # global scope var isi visible in local scope
shadow_vars_1()  # STDOUT: 1
def shadow_vars_2():
    # print(global_scope_var)  # this is even not possible: if I declare local scope var, it shadows global one
                               # and because it's declared AFTER this invocation it's not visible for this line
    # <----- so here's a block where global_scope_var does not exist at all
    global_scope_var = 2
    print(global_scope_var)
shadow_vars_2()  # STDOUT: 2
print(global_scope_var)  # STDOUT: 1
# CONCLUSION: outer scope var can be shadowed, a new variable is defined in this scenario in a local scope,
# and the outer scope var is left untouched

#######################################################################################################################
print("\nlocal and global vars")
def global_local_scope_test():
    def do_local():
        my_var = "shadowed"  # creates own var (shadows all other scopes) and immediately removes it after an invocation

    def do_nonlocal():
        nonlocal my_var  # points to the var from the outer scope (first it's found, possibly)
                         # so, overrides the value from global_local_scope_test() function scope
        my_var = "nonlocal"

    def do_global():
        global my_var  # points to the global scope var (even it doesn't exist right now - then it creates it)
                       # so, creates a new global var but leaves global_local_scope_test() function scope var untouched
        my_var = "global"

    my_var = "local"
    do_local()
    print("after do_local():", my_var)  # STDOUT: after do_local(): local
    do_nonlocal()
    print("after do_nonlocal():", my_var)  # STDOUT: after do_nonlocal(): nonlocal
    do_global()
    print("after do_global():", my_var)  # STDOUT: after do_global(): nonlocal
global_local_scope_test()
print("in global scope:", my_var)  # STDOUT: in global scope: global

#######################################################################################################################
print("\ndeclaring multiple vars")
def declare_multiple_vars():
    a, b = 1, "a"
    print(a, b)
    # a: int, b: string = 1, "a"  # not possible with type hints
declare_multiple_vars()
