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
print (list(range(4)))



