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
    print(global_scope_var)
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
