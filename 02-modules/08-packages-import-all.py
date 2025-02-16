from mypackage.mysubpackage import *

# init __init__.py (see mypackage/mysubpackage/__init__.py) one can define which files are imported by default with *
# wildcard: in this scenario we import mymodule, but not mymodule2

# also in module file (see mypackage/mysubpackage/mymodule.py) in __all__ we can define what exactly can be imported
# from this module using * wildcard

fun3()  # STDOUT: hello from fun3
# fun4()  # ERROR: name 'fun4' is not defined
# fun5()  # ERROR: name 'fun5' is not defined
