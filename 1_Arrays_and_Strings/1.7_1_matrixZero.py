def replaceWithZeroes(input):
	rows = [0]*len(input)
	columns = [0]*len(input[1])
	for i in range(0, len(input)):
		for j in range(0, len(input[1])):
			if input[i][j] == 0:
				rows[i], columns[j]=1, 1
				

	for i in range(0, len(input)):
		for j in range(0, len(input[1])):
			if rows[i] == 1:
				input[i][j] = 0
			if columns[j] == 1:
				input[i][j] =0

	return input

		
input = [[1,2,0],[4,1,6],[0,8,9]]
print (replaceWithZeroes(input))