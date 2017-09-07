student1 = "Mikayla"
student2 = "Jennifer"
student3 = "Nikolas"
student4 = "Zach"

# print student1
# print student2
# print student3
# print student4

# list is a single variable with a bunch of numbered (indexed) parts.
# An index, in a list, is ALWAYS a number (integer)
# A list is made with []. Every element is separated by a ,
students = [
	"Mikayla",
	"Jennifer",
	"Nikolas",
	"Zach"
]

# print students
# print students[0]
# print students[3]
# print students[-1]

# I know the Thrashers are gone
atlanta_teams = [
	'Falcons',
	'Braves',
	'Hawks',
	'Thrashers'
]

# print atlanta_teams
# # Remove an element from the end with "pop"
# atlanta_teams.pop()
# print atlanta_teams

# We have another team. ATL United!
atlanta_teams.append("Atl United")
print atlanta_teams

# Loop from 0-5
# for i in range(0,5):
atlanta_teams_length = len(atlanta_teams)
for i in range(0,atlanta_teams_length):
	# Check to see if the ith element (the one we are on) is thrashers
	# Before we assume there is an ith element, let's "try" so we can have a crash test
	if(atlanta_teams[i] == "Thrashers"):
		thrashers_index = i
		# break means STOP the loop. I don't care about the condition
		break

atlanta_teams.pop(thrashers_index)
print atlanta_teams

# atlanta_teams.pop(3)
# print atlanta_teams

# Split tuns a string into a list.
# It expects a "Delimiter" which is what it's supposed to use to break up the elements in the string
# teams_as_a_string = "Falcons, Braves, Hawks, Atl United"
# print teams_as_a_string
# teams_as_a_list = teams_as_a_string.split(', ')
# print teams_as_a_list

# Lists also have a sort method.
# Beware, Sort will change the list.
# atlanta_teams.sort();
# print atlanta_teams

# Sorted will sort the list, but will NOT chagne the list. 
# Instead, it returns the sorted list
sorted_atlanta_teams = sorted(atlanta_teams)
print atlanta_teams
print sorted_atlanta_teams

sorted_atlanta_teams.reverse()
sorted_atlanta_teams.reverse()
print sorted_atlanta_teams

# if you want to copy a part of the list, you can use [x:y]
# This will create a COPY of the array. It will NOT change the original
# It will start at the Xth element, and will stop at the Yth.
# So if we want Braves and Hawks (1,2), we start at 1, we stop before 3
baseball_basketball = atlanta_teams[1:3]
print baseball_basketball

all_but_the_first = atlanta_teams[1:]
print all_but_the_first
# all_but_the_first = atlanta_teams[1:len(atlanta_teams)]

# to delete an index, you can use the remove method.
# alternative to pop, you provide the element insetad of the index
atlanta_teams.remove("Braves")
print atlanta_teams

# insert... we can insert an element, wherever we want!
atlanta_teams.insert(1,"Braves")
print atlanta_teams

atlanta_teams.insert(0,"Tom Brady's Team")
print atlanta_teams



