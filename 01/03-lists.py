#!/usr/bin/env python3


############################lists
squares = [1, 4, 9, 16, 25]

print (squares)

print (squares[0])		# indexing returns the item
print (squares[-1])
print (squares[-3:])	# slicing returns a new list

# shallow copy
print (squares[:])

# concatenation
print (squares + [36, 49, 64, 81, 100])

# lists are mutable
cubes = [1, 8, 27, 65, 125]		# something's wrong here
print (4**3)					# the cube of 4 is 64, not 65!
cubes[3] = 64					# replace the wrong value
print (cubes)

# add new items at the end of the list
cubes.append(216)				# add the cube of 6
cubes.append(7**3)				# and the cube of 7

print (cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print (letters)

# now remove them
letters[2:5] = []
print (letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print (letters)

# len() also applies to lists
letters = ['a', 'b', 'c', 'd']
print (len(letters))

# nest lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)
print (x[0])
print (x[0][1])





