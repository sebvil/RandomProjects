from math import sqrt

def prime_factors(n):
	if type(n) is not int:
		raise TypeError("Input integer required")
	elif n == 1:
		return []
	elif n == 0:
		return None
	elif n < 0:
		return prime_factors(-n)
	else:
		factors = []
		x = int(sqrt(n))
		for i in range(2,x+1):
			if n % i == 0:
				factors += [i]+prime_factors(n/i)
				break
		if factors == []:
			factors = [n]
		return factors

def is_prime(n):
	if type(n) is not int:
		return False
	elif n < 2:
		return False
	else:
		return len(prime_factors(n)) == 1

def n_primes(n):
	if type(n) is not int:
		raise TypeError("Input integer required")
	if n < 0:
		raise ValueError("Expect input greater than 0, %i given" % n)
	primes = []
	i = 0
	j = 2
	while i < n:
		if is_prime(j):
			primes.append(j)
			i+= 1
		j+=1
	return primes

def pos_factors(n):
	if type(n) is not int:
		raise TypeError("Integer input required")

	else:
		factors = []
		pos = abs(n)
		x = int(sqrt(pos))
		for i in range(1, x+1):
			if n % i == 0:
				factors.append(i)
				if n/i != i:
					factors.append(abs(n/i))
		return sorted(factors)


def gcd(a, b):
	if type(a) is not int or type(b) is not int:
		raise TypeError("Integer input required")
	A = max(abs(a),abs(b))
	B = min(abs(a),abs(b))
	while B>0:
		r = A % B
		A = B
		B = r
	return A

def relatively_prime(a,b):
	return gcd(a,b) == 1

def phi(m):
	primes = prime_factors(m)
	power_counts ={}
	while primes != []:
		i = primes[0]
		count = primes.count(i)
		power_counts[i] = count
		primes = primes[count:]
	prod  = 1
	for prime in power_counts:
		prod *=  (prime-1) * (prime ** (power_counts[prime] -1)) 

	return prod

def d(n):
	return len(pos_factors(n))

def all_factors(n):
	l = []
	for i in pos_factors(n):
		l.append(-i)
	return pos_factors(n)+l

def lcm(a, b):
	return (a * b) / gcd(a,b)

def nth_prime(n):
	return n_primes(n)[n-1]



i =1
while True:
	x = nth_prime(i)
	i = x
	print x
