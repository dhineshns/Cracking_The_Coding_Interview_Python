
path = []
def findPath(x, y):
	path.append([x,y])
	if x==0 & y==0:
		return True
	success = False
	if (not success & x>=1):
		success = findPath(x-1, y)
	if (not success & y>=1):
		success = findPath(x, y-1)
	
	return success

print findPath(3,3)
print path
