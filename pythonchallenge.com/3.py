# Open the file with the encoded message and make it into a string
file = open('3.txt')
messy_string = file.read()
file.close()

# Create two separate alphabets for matching
small = "abcdefghijklmnopqrstuvwxyz"
cap = small.upper()


# Look at each letter, if the three before, and three after, are capital letters
# Skip the first and last three
max_index = len(messy_string)-6
found_matches = ""

for index in range(max_index):
	if messy_string[index] in small:
		if messy_string[index-1] in cap:
			if messy_string[index-2] in cap:
				if messy_string[index-3] in cap:
					if messy_string[index-4] in small:
						if messy_string[index+1] in cap:
							if messy_string[index+2] in cap:
								if messy_string[index+3] in cap:
									if messy_string[index+4] in small:
										found_matches += (messy_string[index])

print(found_matches)
print("done")