# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.
# Python is dnyamic! We don't have a "Declare" step.
# We just make them!.
fullName = "Robert Bunch"
age = 38

# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.

# So... there are no arrays. But there are lists!.
# There is no push... but there is append!.
myArray = [];
myArray.append(fullName)
myArray.append(age)
# there is no "console" in python. But we can print!
print myArray

# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.
# Function = defintion in python.
def say_hello():
	print "Hello!"
say_hello()

# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed 
# in the instructions PDF.

# Easy peasy. Split will do the trick.
splitName = fullName.split()
print splitName

# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)

def sayName():
	print "Hello, %s" % splitName[0]
sayName()

# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.

# datetime is included in Python... we just need to import it!
import datetime
now = datetime.datetime.now()
currentYear = now.year
def myAge(yearBorn):
	print (currentYear - yearBorn)
myAge(1978)

# 7) Using the basic function given below, add code so that sum_odd_numbers 
# will print to the console the sum of all the odd numbers from 1 to 5000.  
# Don't forget to call the function!
# HINT: Consider using a 'for loop'.

def sum_odd_numbers():
	# init a var "sum" at 0 so we can increment it
	sum = 0
	# run a loop from 1-5000 (dont include 5001)
	for i in range(1,5001):
		# check to see if it's odd
		if (i % 2 == 1):
			# odd number!
			sum += i
	print sum
sum_odd_numbers()

def sum_odd_numbers2():
	sum = 0
	# range has a 3rd arg. Step is the thrid, so you can run the 
	# loop by 2s (instead of 1s)
	# for i in range(1,5001,2):
	# 	sum += i
	# print sum
	for i in range(4999, 0, -2):
		sum += i
	print sum

sum_odd_numbers2()

def sum_odd_numbers3():
	i = 1
	sum = 0
	# while 1...is ALWAYS true. This will run forever...
	# while keep_running:
	while 1:
		sum += i
		i += 1
		if (i == 5000):
			break
	print sum
sum_odd_numbers3()

