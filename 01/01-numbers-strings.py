#!/usr/bin/env python3

#this is the first comment
spam = 1 # and this is a second comment
		 # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#################################### numbers
print(2 + 2)

print(50 - 5*6)

print((50 - 5*6) / 4)

print(8 / 5) # division always returns a floating point number

print(17 / 3) # classic division returns a float

print(17 // 3) # floor division discards the fractional part

print(17 % 3) # the % operator returns the remainder of the division

print(5 * 3 + 2) # result * divisor + remainder

print(5 ** 2) # 5 squared

print(2 ** 7) # 2 to the power of 7

width = 20
height = 5 * 9
print(width * height)


#operators with mixed type operands convert the integer operand to floating point:
print(4 * 3.75 - 1)

#three distinct numeric types - integers, floating point numbers and complex numbers
#int, float, Decimal, Fraction, etc
#complex numbers - uses the j or J suffix for the imaginary part. eg 3+5j


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





