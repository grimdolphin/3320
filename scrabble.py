def letterScore(x):
	if x in 'aeilnorstu':
		return 1
	elif x in 'dg':
		return 2
	elif x in 'bcmp':
		return 3
	elif x in 'fhvwy':
		return 4
	elif x in 'k':
		return 5
	elif x in 'jx':
		return 8
	elif x in 'qz':
		return 10
	else:
		return 0

def wordScore(str):
	score = 0
	str.casefold()
	for i in range (len(str)):
		score += letterScore(str[i])
	return score

def main():
	word = (input("Enter a word"))
	print("The score is ", wordScore(word), " .")

if __name__ == "__main__":
	main()
