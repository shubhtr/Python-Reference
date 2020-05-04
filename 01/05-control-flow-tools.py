#!/usr/bin/env python3


######################################################### if

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

######################################################### for

# measure some strings
words = ['cat', 'window', 'defenestrate']

for w in words:
	print(w, len(w))

# modify a collection while iterating over that same collection

users = {"dog" : "active", 
			"cat" : "inactive", 
			"horse" : "active", 
			"pigeon" : "active"}

print (users)

# strategy: iterate over a copy
for user, status in users.copy().items():
	if status == 'inactive':
		del users[user]

print (users)

# strategy: create a new collection
active_users = {}
for user, status in users.items():
	if status == 'active':
		active_users[user] = status


######################################################## range

for i in range(5):
	print (i)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print (i, a[i])

print (range(4))

print (sum(range(4)))

print (list(range(4)))

# loop searches for prime numbers
for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')

# this is correct code - the else clause belongs to the for loop, not the if statement
# a loop's else clause runs when no break occurs (more like the else clause of a try statement)


# continue statement - continues with the next iteration of the loop 
# - so it skips the rest of the statements that come after it 
for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)


# pass statement does nothing. it can be used when a statement is required syntactically
# but the program requires no action

# while True:
#	pass			# Busy-wait for keyboard interrupt (Ctrl+C)

# commonly used for creating minimal classes
class MyEmptyClass:
	pass

# used as a place-holder for a function or conditional body when working on new code, 
# allowing you to keep thinking at a more abstract level. the pass is silently ignored.
def initlog(*args):
	pass			# remember to implement this!




