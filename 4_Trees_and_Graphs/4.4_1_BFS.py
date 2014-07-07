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

def bfs(root): #no linked list. Just BFS implemented
	q = Queue()
	q.put(root)
	while(not q.empty()):
		node =  q.get()
		print node.data
		if(node.left):
			q.put(node.left)
		if(node.right):
			q.put(node.right)

a = BinaryTree()
root = a.addNode(10)
#root = None
a.insert(root,2)
a.insert(root,15)
a.insert(root,17)
a.insert(root,100)
a.insert(root,4)


a.inOrder(root)
print "-------"
bfs(root)