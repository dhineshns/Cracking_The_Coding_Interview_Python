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

def find_n_from_last(ll, n):
	p1, p2 = ll.head, ll.head
	ll.printLL()
	print n
	i=1
	while(i < n):
		p2 = p2.next
		i+=1

	while(p2):
		p2 = p2.next
		p1 = p1.next
	return p1




ll = LinkedList()

for i in range(0,20):
	ll.append(i)

n = int (raw_input("Enter the value for n : "))
node = find_n_from_last(ll, n)
ll.printLL()
print "nth from Last element is : "
print node.contents