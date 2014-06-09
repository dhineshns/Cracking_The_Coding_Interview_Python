def reverse(input):
	output = ''
	for c in range(len(input)-1, -1, -1):
		output += input[c]
	return output


input = raw_input("Enter the string : ")
print (reverse(input))