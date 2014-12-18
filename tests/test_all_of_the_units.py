import unittest
import sys
sys.path.append('../')
from pythonRecipe.grouper import grouper
from pythonRecipe.decorator import deco

class GrouperTest(unittest.TestCase):
	def test(self):
		#for i in grouper(2, 'ABCDEFGHIJK'):
		#	print i
		expected_result = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K']]
		results = list(grouper.grouper().grouperfn(2, 'ABCDEFGHIJK'))
		self.assertEqual(expected_result, results)
	def test_decorator(self):
		@deco.time_dec
		def printFunction(n):
			print "Here is my func!"
		printFunction(10)
		self.assertEqual(0, 0)

if __name__ == '__main__':
	unittest.main()