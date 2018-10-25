from functools import reduce

def nCr(n, r):
	x = n-r
	p = reduce((lambda a,b: a* b), range(x+1, n+1))
	den = reduce((lambda a,b: a*b), range(1, r+1))
	prod  = p/ den
	return prod

