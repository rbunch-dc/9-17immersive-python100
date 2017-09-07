# print "Hello, World"
# print("Hello, WOrld")


# # print "This
# # is multiple lines
# # haha!"

# # this is a comment

# print """
# 	Triple quotes will make
# 	python happy.
# 	Event though this is ugly.
# """
# # variales - strings, letters, numbers, or any other stuff you acn make with a keyboard. 
# # a variable is just a fast way to refer to something else. It DOES NOT make the computer faster. It makes it sloewr
# # In python, there is no declation. It is dynamic. It exists when you make it. 
# # Python is NOT heavily type.
# # 
# # theBestClassInAtlanta = "this class!"

# name = "Robert Bunch"; #this is a string. 

# # Data types
# # - strings - English stuff, for people to read.
# # Numbers - someting with digits and the stuff that goes with them (- or . or e)
# # Floats, integers
# # -- float has a . in it
# # -- integer - has no .
# # Booleans - True or false, 1 or 0, off or on.
# # list -list of things. A single variable with a bunch of like parts
# # dictionary - variable of variable
# # objects - we will deal with this later

# name = "Robert " + "Bunch" # + is a concateante symbol with strings
# first = "Robert"
# last = "Bunch"
# full_name = first + " " + last;
# print full_name
# meaning_of_life = 40 + 2; # + i snow an addition symbol
# forty_two = 84 / 2;
# forty_two = 21 * 2;
# one = 83 % 2;
# print forty_two
# # print "The meaning of life is " + forty_two

# print "-" * 20

# # By argument
# first_name = "Robert"
# last_name ="Bunch"

# # Intermingle english and vars: way 1
# print "Hello {} {}".format(first_name,last_name)
# # Way 2
# print "Hello %s" % "Robert"

# # Floats
# pi = 3.14
# print type(pi)
# makeMeAnInt = int(pi);
# print makeMeAnInt
# print type(makeMeAnInt)
# print .2+.1

# # Booleans
# the_truth = True;
# print type(the_truth)

# addOneToMe = 1
# addOneToMe = addOneToMe + 1
# # addOneToMe++
# addOneToMe += 1
# addOneToMe += 10
# addOneToMe -= 10

# Order of operations is what you learned in the 3rd grade.
# 2 + (3 * 4) = 14, not 24
# 2 + 4 / 2  = 4, not 3
# () overrides everything. Use ()

print "What is your name?"
name =  raw_input(">")
print "Your name is %s" % name

print "What is your age?"
age = raw_input(">")
print "Your age is %d" % int(age)

