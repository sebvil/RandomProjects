def ana(word):
	length = len(word)
	if length == 1:
		return [word]
	else:
		words = []
		used = []
		for i in range(length):
			next =  word[:i]+word[i+1:]
			letter = word[i]
			if letter not in used:
				used.append(letter)
				for j in ana(next):
					words.append(letter+j)
		return words

print ana("a")
print ana("aa")
print ana("abc")
print ana("Chema")


