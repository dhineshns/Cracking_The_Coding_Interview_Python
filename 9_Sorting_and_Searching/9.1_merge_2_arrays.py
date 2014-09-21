def merge(left, right):
	l, r = 0, 0 
	output = []
	for i in range(0, len(left)+len(right)):
		lval = left[l] if l<len(left) else None	
		rval = right[r] if r<len(right) else None
		print lval
		if (lval and rval and lval<rval) or rval is None:
			output.append(lval) 
			l+=1
		if (lval and rval and lval>=rval) or lval is None:
			output.append(rval)
			r+=1
	return output

left = [2,4,6,8]
right = [1,3,5,7]
print merge(left, right)