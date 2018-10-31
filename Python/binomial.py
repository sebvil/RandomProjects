from nCr import nCr

class Binomial(object):

	def __init__(self, n, p):
		self.n = n
		self.p = p
		self.probs = {}
		for i in range(0,n+1):
			self.probs[i] = nCr(n,i) * (p ** i) * (1 - p) ** (n-i)

	def print_probs(self):
		for i in range(0,self.n+1):
			print "n:%i, Successes: %i, p:%r, probability: %r" %(self.n, i, self.p, self.probs[i])
	def check_probs(self):
		return reduce((lambda x,y: x+y), self.probs.values())
	def binomial_pdf(self, i):
		return self.probs[i]
	def binomial_cdf(self, i):
		prob = 0
		for j in range(0,i+1):
			prob += self.probs[j]
		return prob

	def at_most_s(self, i):
		return self.binomial_cdf(i)

	def at_least_s(self,i):
		return 1 - at_most(i-1)
	def at_most_f(self, i):
		return at_least(self.n -i)
	def at_least_f(self, i):
		return at_most(self.n -i)

b = Binomial(5 , 0.5)

b.print_probs()
print b.check_probs()
print b.binomial_pdf(3)
print b.binomial_cdf(3)
