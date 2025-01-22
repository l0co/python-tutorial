#######################################################################################################################
print("no local code block, and can't be easily worked around")
if True:
    localScopeVar = 10  # variable names convention looks inconsistent, here they don't complain I used camel case
print(localScopeVar)  # 10
# conclusion: it looks as a truly misleading inconsistency in relation to other langs because not always
# an inner code block creates a scope; sometimes it creates and sometimes not
# only function, class, etc. creates a local scope, but it's a function, class, etc...
def local_scope_test():
    local_scope_var = 10  # here they complaints about camel case and I have to use snake case
# print(local_scope_var)  # can't: local_scope_var' is not defined

#######################################################################################################################
print("\nshadowing vars")
global_scope_var = 1
def shadow_vars_1():
    print(global_scope_var)
shadow_vars_1()  # 1
def shadow_vars_2():
    # print(global_scope_var)  # this is even not possible, if I declare local var it shadows global_scope_var
                               # and because it's declared AFTER this invocation it's not visible for this line
    # <----- so here's a block where global_scope_var does not exist at all
    global_scope_var = 2
    print(global_scope_var)
shadow_vars_2()  # 2
print(global_scope_var)  # 1
# conclusion: outer scope var can be shadowed, a new variable is defined in this scenario and outer scope var is
# left untouched
