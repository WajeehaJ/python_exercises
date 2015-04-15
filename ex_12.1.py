"""
Exercise 1:
Write a function called sumall that takes any number of arguments and returns their sum.
"""
def sumall(*args):
    sum = 0
    for a in args:
        sum +=a
    return sum


result = sumall(1,2,3)

print result


