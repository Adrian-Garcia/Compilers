from node import Node

class Stack:
	def __init__(self):
		self.head = None

	def push(self, value):
		node = Node(value, None)

		if self.head == None:
			self.head = node
		else:
			prevHead = self.head
			self.head = node
			self.head.next = prevHead

		return True

	def pop(self):
		if self.head == None:
			return 

		headVal = self.head.val
		self.head = self.head.next

		return headVal

	def top(self):
		if self.head:
			return self.head.val

	def isEmpty(self):
		return self.head == None