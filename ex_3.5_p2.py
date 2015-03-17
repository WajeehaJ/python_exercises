

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row():
    print '+', '- ' * 4,

def print_col():
    print '/', ' ' * 8,

def print_rows():
    do_four(print_row)
    print '+'

def print_cols():
    do_four(print_col)
    print '/'

def print_twice():
    print_rows()
    do_four(print_cols)

def print_grid():
    do_four(print_twice)
    print_rows()
    print ' '

print_grid()





