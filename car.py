#!/usr/bin/env python3

class Car():
	def exclaim(self):
		print("i am a car!")

class Yugo(Car):
	def exclaim(self):
		print("I'm a Yugo! Much like a Car, but more Yugoish!")
	def need_a_push(self):
		print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()
