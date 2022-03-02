### Useful functions, tips and tricks ###

# CODING STYLE & TIPS
car_door, car_1 # Are good ways to name a variable. 
# Avoid uppercase I, lower L, and all letter O:s.
# Four spaces = One indentation level
# 79 characters per line is common practice. PEP8 says 99 characters
# 72 comment characters is PEP8 recommendation
# Nesting is when dictionaries are stored in a list, or lists in a dictionary
#	etc.


# TEXT and FORMATING
.lower(), .upper(), .title() # Last one converts to Camel Case
.strip(), .lstrip(), .rstrip() # Removes trailing whitespaces
f"{variable_name}, hello there!" # Creates an f-string
tree_id = tree_label[2:4] # Sets tree_id to the 2nd and 3rd values of tree_label

# NUMBERS
# Operations with floats yeilds another float
** # Double asterix represents exponents
range(x, y, z) # Generates a number series from x to y-1 with z steps
range(x) # Generates a number series from 0 to x-1

# The ZEN of Python
import this # Shows The Zen of Python

# LISTS
# Starting with an empety list and appending items on the go is common practice
foobar = [] # Declares a list
foobar[0] # Accesses the first item of that list
foobar[-1] # Accesses the last item of that list. -2 the second to last, etcc
.append() # Adds an item at the end of a list
.insert(0) # Inserts an item at index 0
del foobar[0] # Deletes item at index 0
.pop(0) # Deletes item at index 0, but it's available to use
.remove("foo") # Removes the "foo" item from the list
.sort() # Sorts a list alphabetically
sorted(foobar) # Temporarly sorts a list alphabetically. 
# reverse=True sorts it in reversed order
.reverse() # Reverses the order of a list
len(foobar) # Gives the length of a list, where [0] is the first item.
list()	# Places the given series into a list
min(), max(), sum() # Returns the min, max, and sum of a list
list[1:4] # Returns the 1,2,3 item of a list. 
# Omit the first variable to start at 0, and the last to include the last item. 
#A third variable allows for skipping items
list_2 = list_1[:] # Copies a list
set() # Returns only the unique items of a list

# TUPLES
my_t = (1, 2) # Generates a tuple with the items 1 and 2
my_1 = (1,) # Note the comma! Generates a tuple with the item 1


# LOOPS
for X in Xs: 	# A for loop that itirates a list, Xs, where X is each item
	print X

squares = [value**2 for value in range(1,11)] # Creates a list of 1^2 to 10^2

# IF STATEMENTS
# Equality is case sensitive. Car =/= car
if a == b:, elif a == c:, else: # Are the three different parts of an if statmnt
in # Returns True if an item is in a list or range

# DICTIONARY
car = {'model': 'tesla s', 'year':'2020'} # Creates a dictionary, where 'model'
# is the "index" or "key", and 'tesla s' is the item or value
car['model'] # Accesses the value of the key 'model'
car = {} # Generates an empety dictionary
car['maker'] = 'Testa' # Adds a key with a value
del car['year'] # REmoves the key-value pair of key 'year'
car.get('cost', "It looks like it's free!") # .get returns a given message if
# the requested key is not definied in the dictionary. Default message is "None"
for k, v in car.items() # Loops through the key-value pairs of car
for k in car.keys() # Loops through the keys of car. This does the same thing
# even without the .keys() function
for v in car.values() # Loops through the values of car
# The loops above can be combined with the sorted() function

# SETS
books = {'harry potter', 'lord of the rings', 'a song of ice and fire'}
# Creates a set of the given items. NOTE! It's very similar to a dictionary...
# ... but it is not a dictionary.