'''
Desarrolla y/o documenta una implementación apropiada para las siguientes clases: STACK (lifo), QUEUE (fifo), 
TABLE/HASH/Hash (order),.. (* las puedes implementar “desde 0” o usar alguna librería “pública” *)

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
		if self.size:
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
		if self.size:
			return self.head.val

	def isEmpty(self):
		return self.size == 0

class Hash:
	def __init__(self):
		self.size = 0
		self.keys = []
		self.data = []

	def add(self, key, val):
		for i in range(len(self.keys)):
			if self.keys[i] > key:
				self.keys.insert(i, key)
				self.data.insert(i, val)
				return

			elif self.data == val:
				return

		self.keys.append(key)
		self.data.append(val)

		self.size += 1

		return True

	def position(self, key):
		low = 0;
		top = len(self.keys) - 1

		while low <= top:
			mid = (top + low) // 2

			if self.keys[mid] < key:
				low = mid + 1

			elif self.keys[mid] > key:
				top = mid - 1

			else:
				return mid

	def get(self, key):
		return self.data[self.position(key)]

	def printAll(self):
		for i in range(len(self.keys)):
			print("  ", self.keys[i], " => ", self.data[i])

	def delete(self, key):
		index = self.position(key)
		self.size -= 1
		del self.keys[index]
		del self.data[index]

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

d = Hash()
d.add(1, "one")
d.add(2, "two")
d.add(6, "six")
d.add(3, "three")
d.add(5, "five")
d.add(4, "four")
d.add(7, "seven")

d.delete(7)

print("\nHash: ", )
d.printAll()

print()
