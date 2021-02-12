from node import Node

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def push(self, value):
		node = Node(value, None)

		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = self.tail.next

		return True

	def pop(self):
		if self.head == None:
			return

		headVal = self.head.val
		self.head = self.head.next

		if self.head == None:
			tail = None

		return headVal

	def front(self):
		if self.head:
			return self.head.val

	def isEmpty(self):
		return self.head == None
