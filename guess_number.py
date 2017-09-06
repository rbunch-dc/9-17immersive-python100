
correct_number = 5;
# print guess
keep_guessing = True
while keep_guessing == True:
	guess = int(raw_input("Guess a number between 1-10\n"))
	if(guess == correct_number):
		print "You Win!"
		keep_guessing = False
	else:
		print "Try again"