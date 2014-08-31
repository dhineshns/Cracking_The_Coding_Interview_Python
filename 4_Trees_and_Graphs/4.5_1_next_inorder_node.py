from Queue import *
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


a = BinaryTree()
root = a.addNode(100)

a.insert(root, 10)
node = a.insert(root, 5)
a.insert(root, 1)


a.inOrder(root)
print "node : " + str(node.data) 
