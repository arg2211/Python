'''
code inspired by Codeacademy Python lesson called "PygLatin"
available here: https://www.codecademy.com/learn/python
'''

print 'Pig Latin Translator' #prints this string

word = raw_input("Type any word:") #word = a string that person inputs after seeing the command 'type any word'
if len(word) > 0 and word.isalpha(): #only prints if the string entered has at least 1 character and all characters are letters only

    word = word.lower() #makes word lowercase
    letter1 = word[0] #get first letter of the word
    letter2 = word[1] #get second letter of the word
    letter3 = word[2] #get third letter of the word

    print word and "nice work!"
else: #prints line below if word does not meet 'if' parameters
    print "that's not a word! please use letters only"
