'''
Exercise 3.4:
A function object is a value you can assign to a variable or pass as an argument....
'''

def do_twice(f, val):
    f(val)
    f(val)

def print_spam(val):
    print val

def do_four(f, val):
    do_twice(f,val)
    do_twice(f,val)

do_twice(print_spam, 3)
do_twice(print_spam, 'cat')
do_four(print_spam, "do_four")
