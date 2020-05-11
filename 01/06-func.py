#!/usr/bin/env python3

def fib(n): 		# write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""   # this is the function's 'docstring'
	a, b = 0, 1
	while a < n:
		print (a, end=' ')
		a, b = b, a+b
	print ()

fib(2000)

f = fib 			# value can be assigned to another name which can then also be used as a function

f(100)

# all functions return a value - even ones without a return statement - they return 'None'

fib(0)

print (fib(0))

def fib2(n):		# return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)		# obj.methodname - equivalent to result = result + [a] - more efficient
		a, b = b, a+b
	return result  
	
# return value from a function - without an expression returns None - falling off the end returns None

f100 = fib2(100)	# call it
print (f100)		# write the result


# default argument values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print (reminder)

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# in keyword - test whether or not a sequence contains a certain value

# scope
i = 5

def f(arg=i):
	print (arg)

i = 6
f()

# IMPORTANT WARNING - the default value is evaluated only once. example below is L

def f(a, L=[]):
	L.append(a)
	return L

print (f(1))
print (f(2))
print (f(3))

# if don't want to share between subsequent calls
def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L

print (f(1))
print (f(2))
print (f(3))


