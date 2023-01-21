import sys

def print_args(*args):
    for arg in args:
        print(arg)

print_args(*sys.argv[1:])