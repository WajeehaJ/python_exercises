def factorial(n):
    space = " " * 4 * n
    print space, "factorial of", n 
    if not isinstance(n, int):
        print 'Factorial is defined for only integers.'
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result  = n * recurse
        print space, "returning result", result
        return result


fact = factorial(5)

