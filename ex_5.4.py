"""
Exercise 5.4:
If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, you can. (If the sum of two
lengths equals the third, they form what is called a "degenerate" triangle.)
"""

def sum(x, y):
    z = x+ y
    return z

def is_triangle(a, b, c):
    if ((sum(a,b) > c or sum(a,c) > b or sum(b,c) >  a) and (not (sum(a,b) == c or sum(a,c) == b or sum(b,c) ==  a ))):
        print "No"
    else:
        print "Yes"

prompt = ("Please enter input the length of 3 stick to check if they can form a triangle or not")
input_a = raw_input(prompt + "\nPlease input a \n")
input_a = int(input_a)
input_b = raw_input("Please input b:\n")
input_b = int(input_b)
input_c = raw_input("Please input c:\n")
input_c = int(input_c)

is_triangle(input_a, input_b, input_c)









