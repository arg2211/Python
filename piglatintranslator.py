'''
code inspired by Codeacademy Python lesson called "PygLatin"
available here: https://www.codecademy.com/learn/python

run in command line by typing:
python piglatintranslator.py
'''

print 'This is a Pig Latin Translator' #prints this string

ay = 'ay'

word = raw_input('Type any word here:') #word = a string that person inputs after seeing the command 'type any word'
if len(word) > 0 and word.isalpha(): #only prints if the string entered has at least 1 character and all characters are letters only

    word = word.lower() #makes word lowercase
    letter1 = word[0] #get first letter of the word *positions in a string start at zero!*
    pigword = word[1:len(word)] + letter1 + ay #concatenate strings with +
    print 'the translation of ' + word + ' is ' + pigword

else: #prints line below if word does not meet 'if' parameters
    print 'that\'s not a word! please use letters only'
