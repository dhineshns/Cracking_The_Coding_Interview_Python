
def isUnique(input):
	checker = [0]*256
	for c in input:
		if (checker[ord(c)] != 1):
			checker[ord(c)] = 1
		else:
			return False
	return True

input = raw_input("Enter the string")
print (isUnique(input))