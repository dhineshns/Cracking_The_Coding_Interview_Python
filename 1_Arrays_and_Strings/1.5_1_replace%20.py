def replaceSpace(input):
	output = ""
	for c in input:
		if c == " ":
			output += "%20"
		else:
			output += c
	return output
input = raw_input("Enter the String : ")
print (replaceSpace(input))