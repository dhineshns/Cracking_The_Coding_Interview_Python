def a2b(a,b):
	xor = a ^ b
	count = 0
	while xor != 0:
		count = count + (xor & 1)
		xor = xor >> 1
	return count

a= int (raw_input("Enter the value of A : "))
b= int (raw_input("Enter the value of B : "))
print "A : " + str(bin(a))
print "B : " + str(bin(b))
print "No. of bits needed to change A to B is : " + str(a2b(a, b))