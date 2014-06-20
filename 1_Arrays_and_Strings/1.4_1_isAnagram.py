def isAnagram(input1, input2):
	if (sorted(input2) == sorted(input1)):
		return True
	else:
		return False
input1 = raw_input("Enter the 1st input : ")
input2 = raw_input("Enter the 2nd input : ")
print (isAnagram(input1, input2))