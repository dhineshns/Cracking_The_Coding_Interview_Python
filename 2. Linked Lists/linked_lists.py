class Node:
	def __init__(self, contents, next=None):
		self.contents = contents
		self.next = next
def printLL(node):
	while(node):
		print (node.contents)
		node = node.next

node1 = Node("one")
node2 = Node("two")
node3 = Node("three")


node1.next = node2
node2.next = node3

printLL(node1)