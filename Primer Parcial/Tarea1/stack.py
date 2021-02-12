import sys
sys.path.append(".")
from node import Node

class Stack:
	def __init__(self):
		self.size = 0
		self.head = None

	def push(self, value):
		node = Node(value, None)

		if self.head == None:
			self.head = node
		else:
			prevHead = self.head
			self.head = node
			self.head.next = prevHead

		self.size += 1

		return True

	def pop(self):
		if self.size == 0:
			return 

		headVal = self.head.val
		self.head = self.head.next
		self.size -= 1

		return headVal

	def top(self):
		if self.size:
			return self.head.val

	def isEmpty(self):
		return self.size == 0