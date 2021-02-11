'''
Desarrolla y/o documenta una implementación apropiada para las siguientes clases: STACK (lifo), QUEUE (fifo), 
TABLE/HASH/DICTIONARY (order),.. (* las puedes implementar “desde 0” o usar alguna librería “pública” *)

Las clases deben contener métodos para soportar las principales operaciones de acceso y manipulación (clásicas).
'''

class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next

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
		return self.head.val

	def isEmpty(self):
		return self.size == 0

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
		return self.head.val

	def isEmpty(self):
		return self.size == 0

class Dictionary:
	pass

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print("Stack: ", end="")
while not s.isEmpty():
	print(s.pop(), end=" ")

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)

print("\nQueue: ", end="")
while not q.isEmpty():
	print(q.pop(), end=" ")

print()