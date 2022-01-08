chooseWord = input("Player 1, choose a word: ")
print("The word chosen is " + chooseWord)
numGuess = input("Player 1, choose the number of guesses allowed: ")

# checks if player 1's number of guesses input is a number
while numGuess.isdigit() == False:
	numGuess = input("Invalid Input, please enter a number: ")

print("The number of guesses allowed is: " + str(numGuess))

word_to_guess = ''
for letter in chooseWord:
	word_to_guess = word_to_guess + '_'

separator = ("*\n*") * 100
print(separator)

print("WORD: " + word_to_guess)
print("GUESSES LEFT: " + numGuess)
guesses = []

while int(numGuess) > 0 and word_to_guess != chooseWord:
	userGuess = input("Player 2, guess a letter: ")

	while userGuess.isalpha() == False:
		userGuess = input("Invalid Input, please enter a letter: ")
	while len(userGuess) != 1:
		userGuess = input("Invalid Input, please enter a letter: ")
	while userGuess in guesses:
		userGuess = input("Invalid Input, already guessed: ")
	guesses.append(userGuess)

	if userGuess in chooseWord:
		print("Correct.")

		for letter_ind in range(len(chooseWord)):
			if chooseWord[letter_ind] == userGuess:
				word_to_guess = word_to_guess[:letter_ind] + userGuess + word_to_guess[letter_ind+1 : ]

	else:
		print("Incorrect. Letter is not in the word.")

	print("WORD: " + word_to_guess)
	numGuess = int(numGuess) -1
	print(" GUESSES LEFT: " + str(numGuess))

if word_to_guess == chooseWord:
	print("Congratulations! You guessed the word!")
else:
	print("Game over.")