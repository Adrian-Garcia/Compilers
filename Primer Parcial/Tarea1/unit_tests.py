'''
Para correr el archivo, usar este comando
python -m unittest unit_tests.py

Desarrolla y/o documenta una implementación apropiada para las siguientes clases: STACK (lifo), QUEUE (fifo), 
TABLE/HASH/Hash (order),.. (* las puedes implementar “desde 0” o usar alguna librería “pública” *)

Las clases deben contener métodos para soportar las principales operaciones de acceso y manipulación (clásicas).
'''
from stack import Stack
from queue import Queue
from hash import Hash

import unittest

class TestStack(unittest.TestCase):
	def test_push(self):
		s = Stack()
		self.assertEqual(s.push(1), True)
		self.assertEqual(s.push("Hello"), True)

	def test_pop(self):
		s = Stack()
		s.push(1)
		self.assertEqual(s.pop(), 1)
		s.push(2)
		self.assertEqual(s.pop(), 2)

	def test_top(self):
		s = Stack()
		s.push(1)
		self.assertEqual(s.top(), 1)
		s.push(2)
		self.assertEqual(s.top(), 2)

	def test_isEmpty(self):
		s = Stack()
		self.assertEqual(s.isEmpty(), True)
		s.push(1)
		self.assertEqual(s.isEmpty(), False)

class TestQueue(unittest.TestCase):
	def test_push(self):
		q = Queue()
		self.assertEqual(q.push(1), True)
		self.assertEqual(q.push("Hello"), True)

	def test_pop(self):
		q = Queue()
		q.push(1)
		self.assertEqual(q.pop(), 1)
		q.push(2)
		self.assertEqual(q.pop(), 2)

	def test_front(self):
		q = Queue()
		q.push(1)
		self.assertEqual(q.front(), 1)
		q.push(1)
		self.assertEqual(q.front(), 1)
		q.pop()
		q.pop()
		q.push(2)
		self.assertEqual(q.front(), 2)

	def test_isEmpty(self):
		q = Queue()
		self.assertEqual(q.isEmpty(), True)
		q.push(1)
		self.assertEqual(q.isEmpty(), False)

class TestHash(unittest.TestCase):
	def test_add(self):
		h = Hash()
		self.assertEqual(h.add(1, 2), True)
		self.assertEqual(h.get(1), 2)
		h.add(1, 3)
		self.assertEqual(h.get(1), 3)

	def test_position(self):
		h = Hash()
		h.add(1, 1)
		h.add(0, 0)
		h.add(3, 3)
		h.add(2, 2)
		self.assertEqual(h.position(1), 1)

	def test_get(self):
		h = Hash()
		h.add(1, "one")
		h.add(0, "zero")
		h.add(3, "three")
		h.add(2, "two")
		self.assertEqual(h.get(1), "one")

	def delete(self):
		h = Hash()
		h.add(1, "one")
		self.assertEqual(len(h.zeys), 1)
		h.delete(1)
		self.assertEqual(len(h.zeys), 0)
