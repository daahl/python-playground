# open the file with the encoded message and make it into a string
messy_file = open('mess.txt')
messy_string = messy_file.read()
messy_file.close()

# create a dictionary to keep count of each character occurance
unique_letters = set(messy_string)
letter_counter = {}
for unique in unique_letters:
	counter = 0
	for letter in messy_string:
		if letter == unique:
			counter += 1
	letter_counter[unique] = counter

# add the rarest characters to a new string
rare_characters = ""
for key, value in letter_counter.items():
	if value == 1:
		rare_characters += key

print(rare_characters)
# Using a scrabble word finder, the word is "equality"