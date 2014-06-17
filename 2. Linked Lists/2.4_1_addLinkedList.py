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

def add (val1, val2, carry):
	return val1+val2+carry
def addLL(ll1, ll2):
	node1 = ll1.head
	node2 = ll2.head
	output = LinkedList()
	carry = 0
	while(node1 and node2):
		sum = add(node1.contents, node2.contents, carry)
		if sum>9:
			carry = 1
			sum=sum%10
		else:
			carry = 0
		output.append(sum)
		node1= node1.next
		node2= node2.next

	output.append(carry)
	return output

ll1 = LinkedList()
ll2 = LinkedList()

ll1.append(6)
ll1.append(2)
ll1.append(7)
ll2.append(9)
ll2.append(8)
ll2.append(6)

output = addLL(ll1, ll2)
output.printLL()