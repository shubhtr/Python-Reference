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


