
# A function (in Python "definition"), is a piece of cod that can be
# called from somewhere else. They are meant to be re-usable and to make
# things clean.
# If you have complicated code, you can break it into pieces that are 
# easier to understand.
# Repeating yourself is BAD.
# - Copy and paste errors
# - odd behavoior
# - etc...
# to decare a function in python, you use "def"
# functions ALWAYS have a ()

# This defines the function.
# def say_hello():
	# print "Hello"

# This calls the function (tells Python to run the code inside say_hello def)
# say_hello()

# Passing variables into functions, are called arguments on the way in
# parameters once inside.
# def say_hello_with_name(name):
# 	print "Hello, %s" % name

# say_hello_with_name("Jamie")
# say_hello_with_name("Saif")
# say_hello_with_name("Zach")
# say_hello_with_name("Casey")

# students = ['Jamie','Saif','Zach','Casey']
# for i in range(0,len(students)):
# 	say_hello_with_name(students[i])

say_hello_with_name() #THIS WILL FAIL!!