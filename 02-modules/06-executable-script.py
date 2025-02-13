#!/usr/bin/env python3

# run me as linux executable and give me some arguments

if __name__ == "__main__":  # this is how I know I'm run as executable, not imported as a module
    import sys
    print(sys.argv)  # STDOUT: ['./06-executable-script.py']
                     # (in case called with no additional arguments)

# of course the above "if" does not make sense for Python script which are intended to be used only as executable
# scripts: in this scenario you can start coding right away

