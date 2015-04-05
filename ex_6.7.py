"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.
"""
def is_power(a, b):
    if (a == b):
        return True
    elif(a%b != 0):
        return False
    elif (is_power(int(a/b), b)):
        return True
    else:
        return False

a = raw_input("Please enter a:")
a = int(a)
b = raw_input("Please enter b:")
b = int(b)

if (is_power(a,b) == True):
    print a," is power of ", b
else:
    print a," is not a power of ", b
