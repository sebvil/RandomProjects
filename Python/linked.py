class LinkedList(object):
	def __init__(self,value, child= None):
		args = [ "value", "child"]
		self.value = value
		self.child = child

	def add(self, val):
		if self.child is None:
			self.child = LinkedList(val)
		else:
			self.child.add(val)
	def to_arr(self):
		if self.child is None:
			return [self.value]
		else:
			return [self.value]+self.child.to_arr()

	def print_list(self):
		print self.to_arr()

	def length(self):
		if self.child is None:
			return 1
		else:
			return self.child.length() + 1

	def get_item(self, i):
		if i > 0 and self.child is None:
			raise IndexError("linked-list index out of range")
		elif i == 0:
			return self.value
		elif i< 0:
			l = self.length()
			if -i == l:
				return self.value
			else:
				return self.child.get_item(i)
		else:
			return self.child.get_item(i-1)
	def find(self, i):
		if self.child is None:
			return "Not found"
		if self.value == i:
			return 0
		else:
			s = self.child.find(i)
			if type(s) is int:
				return s+1
			else:
				return s

x = LinkedList(0)
y = LinkedList(value = 3)
z = LinkedList(3, 2)


for i in range(1, 5):
	x.add(i)

x.print_list()

for i in range(0,5):
	print x.get_item(i)

for i in range(-1,-6, -1):
	print x.get_item(i)

print x.find(3)
print x.find(6)
