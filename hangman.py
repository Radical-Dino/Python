import random
HANGMANPICS = ['''

  
      
      
      
      
      
=========''', '''


      
      
      |
      |
      |
=========''', '''


      |
      |
      |
      |
      |
=========''', '''

  +---+
      |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def displayBoard(HANGMANPICS, wrongLetters, correctLetters, randomWord):
	print (HANGMANPICS[len(wrongLetters)])
	print ("you've taken %d incorrect guesses" % len(wrongLetters))

	for letter in wrongLetters:
		print(letter)

	blanks = '-' * len(randomWord)

	for i in range(len(randomWord)):
		if randomWord[i] in correctLetters:
			blanks = blanks[:i] + randomWord[i] + blanks [i+1:]
	print(blanks)

def getGuess(alreadyGuessedLetters):
	while True:
		guess=input("Take a guess.")
		guess=guess.lower()
		if len(guess)!=1:
			print ("Plese type a single letter.")
		elif guess not in"abcdefghijklmnopqrstuvwxyz":
			print ("Not a letter.\nPlease type in a letter.")
		elif guess in alreadyGuessedLetters:
			print ("You already guessed this letter.")
		else: 
			return guess

def getRandomWord(wordList):
	wordIndex = random.randint(0, len(wordList.split())-1)
	return wordList.split()[wordIndex]

words = 'zombie computer poopypants dinosaur lightning mountain toilet television object unidentified watermelon forest engine bracelet twenty dustbin hangman connect sun investigate police grandma pteranodon excavator jupiter alien rocket bottle physics concert goldilocks'
print ("H A N G M A N")
wrongLetters = ""
correctLetters = ""
gameover = False
randomWord = getRandomWord(words)


while True:
	displayBoard(HANGMANPICS, wrongLetters, correctLetters, randomWord)
	guess = getGuess(wrongLetters + correctLetters)
	if guess in randomWord:
		correctLetters = correctLetters + guess
		foundAllLetters = True
		for i in range(len(randomWord)):
			if randomWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print ('Yes! The word is ' + randomWord)
			gameover = True

	else:
		wrongLetters = wrongLetters + guess

		if (len(HANGMANPICS)- 1) == len(wrongLetters):
			displayBoard(HANGMANPICS, wrongLetters, correctLetters, randomWord)
			print("You've lost!!!")
			print ("The word is " + randomWord)
			gameover = True

	if gameover:
		answer = input("Do you want to play again?")
		answer.lower()
		if answer == "yes":
			randomWord = getRandomWord(words)
			gameover =False
			correctLetters = ""
			wrongLetters = ""
		else:
			break 




