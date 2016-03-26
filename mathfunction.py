'''
This is a function called 'mathfun' where there are two parameters, n1 and n2.  We call 'mathfun' with the arguments 1 and 30 in the last line.
'''

def mathfun(n1, n2):
    base = n1 + n2
    exponent = n1 - n2
    result = base**exponent
    print "First you entered %d, then you entered %d. I added them together to get your base, %d.  I subtracted the second entry from the first to get your exponent, %d.  %d to the power of %d is %d!" % (n1, n2, base, exponent, base, exponent, result)

mathfun(1, 30)
