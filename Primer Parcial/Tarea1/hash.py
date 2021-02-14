class Hash:
	def __init__(self):
		self.keys = []
		self.data = []

	def add(self, key, val):
		for i in range(len(self.keys)):
			if self.keys[i] > key:
				self.keys.insert(i, key)
				self.data.insert(i, val)
				return

			elif self.keys[i] == key:
				self.data[i] = val

		self.keys.append(key)
		self.data.append(val)

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
		del self.keys[index]
		del self.data[index]
