from random import randint


def monty(switch, not_switch):
	money = randint(0,2)
	choice = randint(0,2)
	if choice != money:
		switch+=1
	else:
		not_switch += 1
	return [switch, not_switch]
switches = []
not_switches = []

arr= [0, 0]
for j in range(0,1):
	for i in range(0,10000000):
		arr = monty(arr[0], arr[1])
	switches.append(arr[0])
	not_switches.append(arr[1])
	arr = [0, 0]
print "switch: %r" % switches 
print "not switch: %r" % not_switches
