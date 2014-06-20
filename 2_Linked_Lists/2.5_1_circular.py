class Node:
	def __init__(self, contents, next = None):
		self.contents = contents
		self.next = next
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	def append(self, node):
		node = Node(node)
		if (self.head == None and self.tail == None) :
			self.head = node
			self.tail = node
		elif (self.tail) :
			self.tail.next = node
			self.tail = node		
	def printLL(self):
		print "The Linked List :"
		node = self.head
		while(node):
			print node.contents
			node = node.next
def findCircleStart(ll):
	node1 = ll.head
	node2 = ll.head
	node1 = node1.next
	node2 = node2.next.next
	while(node1 != node2):
		node1 = node1.next
		node2 = node2.next.next

	node1 = ll.head

	while(node1 != node2):
		node1 = node1.next
		node2 = node2.next

	return node1.contents

ll = LinkedList()
for i in range(1,10):
	ll.append(i)
tmp = ll.head
for i in range(1, 4):
	tmp = tmp.next
ll.tail.next = tmp

print findCircleStart(ll)
