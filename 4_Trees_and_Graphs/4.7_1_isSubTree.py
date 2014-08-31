from Queue import *
class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
class BinaryTree:
	def __init__(self):
		self.root = None
		self.inString = ""

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
			self.inString = self.inString + (str(root.data))
			print root.data
			self.inOrder(root.right)


a = BinaryTree()
b = BinaryTree()
rootA = a.addNode(10)
#root = None
a.insert(rootA,2)
a.insert(rootA,15)
a.insert(rootA,17)
a.insert(rootA,100)
a.insert(rootA,4)

rootB = b.addNode(10)
#root = None


a.inOrder(rootA)
b.inOrder(rootB)
if b.inString in a.inString:
	print "SubTree"
else:
	print "!SubTree"