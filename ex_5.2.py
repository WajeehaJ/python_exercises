"""
Write a function called do_n that takes a function object and a number, n,
as arguments, and that calls the given function n times.
"""

def print_hello():
    print "Hello"

def do_n(f,n):
    if(n<=0):
        return
    else:
        f()
        do_n(f, n-1)

do_n(print_hello, 3)
