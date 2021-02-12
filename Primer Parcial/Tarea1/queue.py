import sys
sys.path.append(".")
from node import Node

class Queue:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def push(self, value):
		node = Node(value, None)

		if self.size == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = self.tail.next

		self.size += 1
		return True

	def pop(self):
		if self.size == 0:
			return

		headVal = self.head.val
		self.head = self.head.next

		self.size -= 1
		if self.size == 0:
			tail = None

		return headVal

	def front(self):
		if self.size:
			return self.head.val

	def isEmpty(self):
		return self.size == 0
