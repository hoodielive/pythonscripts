import unittest 

def divide_by_one(x):
	return x / 1

class DividedByOneTest(unittest.TestCase):
	def test(self):
		self.assertEqual(divide_by_one(4),4)