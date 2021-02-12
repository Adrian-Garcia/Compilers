'''
Desarrolla y/o documenta una implementación apropiada para las siguientes clases: STACK (lifo), QUEUE (fifo), 
TABLE/HASH/Hash (order),.. (* las puedes implementar “desde 0” o usar alguna librería “pública” *)

Las clases deben contener métodos para soportar las principales operaciones de acceso y manipulación (clásicas).
'''
from stack import Stack
from queue import Queue
from hash import Hash

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
