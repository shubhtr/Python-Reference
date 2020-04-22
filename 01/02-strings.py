#!/usr/bin/env python3

######################################### strings

print('spam eggs') # single quotes

print('doesn\'t') # use \' to escape the single quote

print("doesn't") # ... or use double quotes instead

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.' # \n means newline
print (s)

print('C:\some\name') # here \n means newline!

print(r'C:\some\name') # note the r before the quote - for 'raw strings'

# string literals spanning multiple lines - triple quotes: """...""" or '''...'''
print("""\
Usage: thingy [OPTIONS]
	-h						Display this usage message
	-H	hostname			Hostname to connect to 
""")

# strings can be concatenated together with the + operator, and repeated with *

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

print('Py' 'thon')

text = ('Put several things within parentheses '
		'to have them joined together.')
print(text)

prefix = 'Py'
#prefix 'thon' # can't concatenate a variable and a string literal
#('un' * 3) 'ium'

print(prefix + 'thon') # use '+' to concatenate variables or a variable and a literal

# indexing
word = 'Python'
print (word[0]) 	# character in position 0
print (word[5]) 	# character in position 5
print (word[-1])	# last character
print (word[-2])	# second-last character
print (word[-6])

# slicing
print (word[0:2]) 	# characters from position 0 (included) to 2 (excluded)
print (word[2:5])	# characters from position 2 (included) to 5 (excluded)

# start is always included and end is always included
# this makes sure that s[:i] + s[i:] is always equal to s
print (word[:2] + word[2:])
print (word[:4] + word[4:])

#useful defaults:
#omitted first index defaults to zero,
#omitted second index defaults to the size of the string being sliced
print (word[:2])	# character from the beginning to position 2 (excluded)
print (word[4:])	# character from position 4 (included) to the end
print (word[-2:])	# characters from the second-last (included) to the end

#word[42] # error - string index out of range

#handled gracefully
print (word[4:42])
print (word[42:])

# strings immutable
# word[0] = 'J' 	# error

print ('J' + word[1:])
print (word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print (len(s))



