class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
class BinaryTree:
	def __init__(self):
		self.root = None


	def insert(self, root, data):
		if root==None:
			root = Node(data)
		else:
			if root.data >= data:
				root.left = self.insert(root.left, data)
			elif root.data < data:
				root.right = self.insert(root.right, data)
		return root
	def preOrder(self, root):
		if (not root==None):
			self.preOrder(root.left)
			print root.data
			self.preOrder(root.right)

a = BinaryTree()
root = None
root = a.insert(root,2)
#root = None
a.insert(root,4)
a.insert(root,34)
a.insert(root,45)
a.insert(root,46)
a.insert(root,41)
a.insert(root,48)
a.preOrder(root)


