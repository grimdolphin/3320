import random
option = int(input("""Enter 1 for a random word from a list,
enter 2 for a random word from external file,
or enter 3 for random word from an internet dictionary."""))
if option == 1:
	x = [['f','a','r'], ['c','a','r'], ['b','a','r']]
	A = random.choice(x)
elif option == 2:
	file = str(input("What is the name of the file?"))
	A = random.choice(open(file).read().split().split())
else:
	A = ['h','a','n','g','m','a','n']
L = ['_'] * (len(A))
play = True 
wrong = 0
while play == True: 
	# Ask the user to guess a letter 
	letter = str(input("Guess a letter: ")) 
	# Check to see if that letter is in the Answer 
	for i in range (len(A)): 
	# If the letter the user guessed is found in the answer, # set the underscore in the user's answer to that letter 
		
		if letter == A[i]: 
			L[i] = letter 
			i = i + 1 
			# Display what the player has thus far (L) with a space 
			# separating each letter 
			print(' '.join(str(n) for n in L)) 
			# Test to see if the word has been successfully completed, 
			# and if so, end the loop
		if letter not in A:
			print("BAD GUESS!")
			wrong += 1
			if wrong == 6:
				print("Game over")
				quit()
			break
	if A == L: 
		play = False 
		print("GREAT JOB!") 

