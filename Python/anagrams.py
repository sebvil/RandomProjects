import argparse

def ana(word):
	word = word.lower()
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



ap = argparse.ArgumentParser()
ap.add_argument("-w", "--word", required = True, help = "Word to find the anagrams of")
args = vars(ap.parse_args())


try:
	word = args["word"]
	ans =  ana(word)
	print ans
	print len(ans)
except AttributeError:
	pass
