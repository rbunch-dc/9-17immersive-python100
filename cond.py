# if(1 == 2):
# 	print "True!"
# print "False"

# if(1 == 2):
# 	print "True!"
# else:
# 	print "False"

# if(1 == 2):
# 	print "True!"
# elif(2 == 3):
# 	print "Second one is true!"
# else:
# 	print "False"

classSize = 19;
question = "How big is your class?";
print question
response = raw_input("> ")
# Remember, raw_input is always collected as a string...
response_as_an_int = int(response)
if(response_as_an_int != classSize):
	print "You must not be in the September class."
else:
	print "Let's learn to code!"

# Random is a python module, that comes with python.
import random;
rand_number = random.randint(1,10)
print rand_number

# Loops
# A while loop, will run forver or until the condition is false
keep_going = True
while keep_going:
	get_answer = raw_input("Please hit any key")
	keep_going = False
print "You are no longer in the loop!"


