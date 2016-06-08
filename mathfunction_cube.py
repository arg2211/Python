'''
This is a simple function using an "if else" statement.
'''

def cube(number):
    print number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        print "That number is not divisible by 3 - try again!"

number = int(raw_input("Choose a number: "))

by_three(number)
