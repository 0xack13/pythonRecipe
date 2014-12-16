import unittest
import sys
sys.path.append('../')
from pythonRecipe.grouper import grouper

class GrouperTest(unittest.TestCase):
	def test(self):
		#for i in grouper(2, 'ABCDEFGHIJK'):
		#	print i
		expected_result = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K']]
		results = list(grouper.grouper().grouperfn(2, 'ABCDEFGHIJK'))
		self.assertEqual(expected_result, results)

if __name__ == '__main__':
	unittest.main()