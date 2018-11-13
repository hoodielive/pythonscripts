# Functions - pass args 

def parameters(a):
	print(a)

parameters(3)

def add(a,b):
	c = a + b 
	return c

result = add(12,5)

print(result)

def default_param(a,b=4,c=5):
	return a + b + c 
result = default_param(3,2,1)

print(result)

def scope(a):
	a = a + 1 
	print(a)
	return a 

scope(5)

def outer(a):
	def nested(b):
		return b * a 
	a = nested(a)
	return a

print(outer(4))

def f(a):
	def g(b):
		def h(c):
			return a * b * c
		return h

	return g

print(f(5)(2))