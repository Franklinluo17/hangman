import fileinput
from random import randint
dictionary = []
for line in fileinput.input():
	dictionary.append(str(line))
word = dictionary[randint(0,len(dictionary)-1)]
word = word.lower()
counter = int(raw_input("how many guesses do you want?"))
hangman = ["_" for x in range(len(word)-1)]
print word
already_guessed = []
while(counter > 0):
	guess = raw_input("enter your guess of a letter from a-z ")
	already_guessed.append(guess)
	if word.find(guess) == -1:
		print "Your guess is not in the word"
		counter -= 1
	else:
		while(word.find(guess) != -1):
			hangman[word.find(guess)] = guess
			word = word.replace(guess,"_",1)
	if "_" not in hangman:
		break
	print hangman
	print "You've already guessed" 
	print already_guessed
	print "You have %s guesses remaining" %(counter) 
	print "\n"
if(counter == 0):
	print "You lose"
else:
	print "Congragulations, You Won!"

