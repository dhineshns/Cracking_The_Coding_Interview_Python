class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
class BinaryTree:
	def __init__(self):
		self.root = None

	def addNode(self, data):
		return Node(data)
	def insert(self, root, data):
		if root==None:
			root = self.addNode(data)
		else:
			if root.data >= data:
				root.left = self.insert(root.left, data)
			elif root.data < data:
				root.right = self.insert(root.right, data)
		return root
	def inOrder(self, root):
		if (not root==None):
			self.inOrder(root.left)
			print root.data
			self.inOrder(root.right)
def maxDepth(root):
	if root == None:
		return 0
	maximum = 1 + max(maxDepth(root.left), maxDepth(root.right))
	return maximum
def minDepth(root):
	if root == None:
		return 0
	maximum = 1 + min(maxDepth(root.left), maxDepth(root.right))
	return maximum
def isBalanced(root):
	if ((maxDepth(root)-minDepth(root) == 0) or (maxDepth(root)-minDepth(root) == 1)):
		return True
	else:
		return False

a = BinaryTree()
root = a.addNode(2)
#root = None
a.insert(root,45)
a.insert(root,35)
a.insert(root,4)
a.insert(root,41)
a.insert(root,45)
a.insert(root,5)
a.insert(root,47)
a.insert(root,22)
a.inOrder(root)
print "max : "+str(maxDepth(root))
print "min : "+str(minDepth(root))
print isBalanced(root)

