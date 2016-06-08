'''
This is a function called 'mathfun' where there are two parameters, n1 and n2.
We can call 'mathfun' with the arguments n1 and n2 in the last line.
n1 and n2 are input by the user.
'''

# define the function, called 'mathfun' and put names of parameters inside parentheses
def mathfun(n1, n2):
    # define variables named 'base', 'exponent', and 'result'
    base = n1 + n2
    exponent = n1 - n2
    result = base**exponent
    # and tell the function what to print
    print "First you entered %d, then you entered %d. I added them together to get your base, %d.  I subtracted the second entry from the first to get your exponent, %d.  %d to the power of %d is %d!" % (n1, n2, base, exponent, base, exponent, result)

n1 = int(raw_input("Pick a number:"))
n2 = int(raw_input("Pick another number:"))
mathfun(n1, n2)
