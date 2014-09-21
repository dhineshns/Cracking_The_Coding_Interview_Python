def allSubsets(s):
	maximum = 1 << len(s)
	output = []

	for i in range(0,maximum):
		subset = []
		k = i
		index = 0
		while(k > 0):
			if k & 1:
				subset.append(s[index])
			k = k >>1
			index = index + 1
		output.append(subset)
	return output

s = [1,2,3]
print allSubsets(s)