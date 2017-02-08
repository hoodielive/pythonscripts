#!/usr/bin/env python3

class Person:
	count = 0 
	def __init__(self, name, age):
		self.name = name
		self.age = age 
		Person.count += 1 

	def changeAge(self, age):
		self.age = age 

	def getCount(self):
		return Person.count 

	def __str__(self): 
		return self.name + '--' + str(self.age)

p1 = Person('Hoodie', 20)
print(p1)
print(p1.getCount())

p2 = Person('Vinny', 23)
print(p2)
print(p2.getCount())

p2.changeAge(19)
print(p2)
print(p2.getCount())