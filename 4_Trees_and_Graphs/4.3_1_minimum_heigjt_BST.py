class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

def createBalancedBST(sorted_array, start, end):
	if start > end:
		return None
	mid = ((start + end)/2)

	tNode = Node(sorted_array[mid])
	tNode.left = createBalancedBST(sorted_array, start, mid-1)
	tNode.right = createBalancedBST(sorted_array, mid+1, end)
	return tNode
def inOrder(root):
	if (not root==None):
		inOrder(root.left)
		print root.data
		inOrder(root.right)

sorted_array = [1,2,3,4,5,6,7]
tNode = createBalancedBST(sorted_array, 0, len(sorted_array)-1)
inOrder(tNode)
