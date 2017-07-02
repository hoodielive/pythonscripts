#!/usr/bin/env python3

class Person():
	def __init__(self,name):
		self.name = name 

class MDPerson(Person):
	def __init__(self, name):
		self.name = "Doctor " + name 

class JDPerson(Person):
	def __init__(self, name):
		self.name = name + ", Esquire"

class emailPerson(Person):
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email 

person = Person('hoodie')
doctor = MDPerson('hilbert')
lawyer = JDPerson('karla')

print(person.name)
print(doctor.name)
print(lawyer.name)

hoodies = emailPerson('hoodie phrekles', 'hoodie@phrekles.com')

print(hoodies.name) 
print(hoodies.email) 
