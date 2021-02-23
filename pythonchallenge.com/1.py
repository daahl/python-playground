encoded_mess = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = "abcdefghijklmnopqrstuvwxyzab"
alphabet_2 = "cdefghijklmnopqrstuvwxyzabcd"
decoded_mess = ""

print(alphabet.index("g"))

for letter in encoded_mess:
	if letter in alphabet:
		index = alphabet.index(letter)
		decoded_mess += alphabet[index + 2]
	else:
		decoded_mess += letter


print(decoded_mess)

string = "map"
table = string.maketrans(alphabet, alphabet_2)

print(string.translate(table))