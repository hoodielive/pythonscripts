# Recursive Functions 

def factorials(n):
	if n == 1:
		return 1 
	else:
		return n * factorials(n - 1)

print(factorials(5))

# regular recursion 

def sums(n):
	if n == 1:
		return 1 
	else:
		return n + sums(n-1)

result = sums(3) 
print(sums)

# Tail 

def tail_sums(n, accumulator = 0):
	if n == 0:
		return accumulator
	else:
		return tail_sums(n-1, accumulator+n)
print(sums(10))
print(tail_sums(10))