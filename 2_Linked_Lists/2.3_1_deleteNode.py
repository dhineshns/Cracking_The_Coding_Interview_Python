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
def deleteNode(node):
	nextNode = node.next
	node.contents = nextNode.contents
	node.next = nextNode.next
	return True


ll = LinkedList()

for i in range(0,20):
	ll.append(i)
print ("Before:")
ll.printLL()
node = ll.head
for i in range(0, 7):
	node = node.next
deleteNode(node)
print ("After:")
ll.printLL()