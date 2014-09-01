def insert_bits(N, M, i, j):
	mask = 0b1111111111111111
	mask = mask << j
	right = (1 << i) -1
	mask = mask | right

	print "mask : " + str(bin(mask))

	return (N & mask) | (M << i)


N = 0b100010001000
M = 0b1111

print "The value of N is " + str(bin(N))
print "The value of M is " + str(bin(M))

i= int(raw_input("Enter the pointer value for i : "))
j= int(raw_input("Enter the pointer value for j : "))

print str(bin(insert_bits(N, M, i, j)))
