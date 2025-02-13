from mypackage.mysubpackage.mymodule import *

# init __init__.py (see mypackage/mysubpackage/__init__.py) one can define which files are imported by default with *
# wildcard: in this scenario we import mymodule, but not mymodule2

fun3()  # STDOUT: hello from fun3
# fun5()  # ERROR: name 'fun5' is not defined
