#!/usr/bin/env python3

x = int(input("Please enter an integer: "))

if x < 0:
	x = 0 
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

# if...elif...elif ... sequence is a substitute for the switch or case statements found in other languages

