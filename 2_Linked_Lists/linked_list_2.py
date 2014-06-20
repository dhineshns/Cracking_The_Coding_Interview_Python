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
		node = self.head
		while(node):
			print node.contents
			node = node.next

ll = LinkedList()
option = 0
while option !=3:
	option = int (raw_input("----Linked list----\n 1. Append \n 2. Print  \n 3. Exit \n "))
	if (option == 1) : 
		ll.append(raw_input("Enter the number to be appended : "))
	elif option == 2 :
		ll.printLL()




