"""
Exercise 5.3: Related to Fermat Theorem
      a.pow(n) + b.pow(n) = c.pow(n)
      solution is non-zero for values of n > 2
"""

from math import pow

def check_fermat(a, b, c, n):
    if n > 2 and (pow(c,n) == (pow(a,n)+ pow(b,n))):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

prompt = "Check fermat's last theorem a.pow(n) + b.pow(n) = c.pow(n) for n > 2\n"
input_a = raw_input(prompt + "\nPlease input a \n")
input_a = int(input_a)
input_b = raw_input("Please input b:\n")
input_b = int(input_b)
input_c = raw_input("Please input c:\n")
input_c = int(input_c)
input_n = raw_input("Please input n:\n")
input_n = int(input_n)

check_fermat(input_a, input_b, input_c, input_n)
