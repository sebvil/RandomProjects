from functools import reduce

def nCr(n, r):
	if r == 0:
		return 1
	den = factorial(r)

	num = reduce((lambda x,y: x*y), range(n-r+1, n+1))
	prod  = num / den
	return prod


def factorial(n):
	if n == 0:
		return 1
	else: 
		return reduce((lambda x,y: x * y), range(1,n+1))

