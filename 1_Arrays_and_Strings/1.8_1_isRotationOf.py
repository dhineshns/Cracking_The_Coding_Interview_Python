def isRotationOf(input1, input2):
	if   input1 in input2+input2:
		return True
	else:
		return False
input1 = raw_input("Enter the first string : ")
input2 = raw_input("Enter the second string : ")

print (isRotationOf(input1, input2))