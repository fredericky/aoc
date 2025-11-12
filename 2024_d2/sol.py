import unittest
from typing import List

def is_safe(report: List[int]) -> bool:
	increasing = True if report[0] < report[1] else False
	for i in range(1, len(report)):
		diff = report[i] - report[i-1]
		if (increasing and diff <= 0) or (not increasing and diff >= 0):
			return False
		if not (1 <= abs(diff) <= 3):
			return False
	return True

def is_almost_safe(report: List[int]) -> bool:
	if is_safe(report):
		return True
	
	for i in range(len(report)):
		modified_report = report[:i] + report[i+1:]
		if is_safe(modified_report):
			return True
	
	return False

def solve_p1():
	with open("./input", "r") as f:
		safe_count = 0
		for line in f:
			report = list(map(int, line.split()))
			if is_safe(report):
				safe_count += 1
	print(safe_count)

def solve_p2():
	with open("./input", "r") as f:
		almost_safe_count = 0
		for line in f:
			report = list(map(int, line.split()))
			if is_almost_safe(report):
				almost_safe_count += 1
	print(almost_safe_count)

class Tests(unittest.TestCase):
	def test_is_safe(self):
		self.assertEqual(is_safe([7,6,4,2,1]), True)  # Safe: all decreasing by 1 or 2
		self.assertEqual(is_safe([1,2,7,8,9]), False)  # Unsafe: 2->7 is increase of 5
		self.assertEqual(is_safe([9,7,6,2,1]), False)  # Unsafe: 6->2 is decrease of 4
		self.assertEqual(is_safe([1,3,2,4,5]), False)  # Unsafe: changes direction
		self.assertEqual(is_safe([8,6,4,4,1]), False)  # Unsafe: 4->4 is no change
		self.assertEqual(is_safe([1,3,6,7,9]), True)  # Safe: all increasing by 1, 2, or 3
	
	def test_is_almost_safe(self):
		self.assertEqual(is_almost_safe([7,6,4,2,1]), True)  # Safe without removing any level
		self.assertEqual(is_almost_safe([1,2,7,8,9]), False)  # Unsafe regardless of which level is removed
		self.assertEqual(is_almost_safe([9,7,6,2,1]), False)  # Unsafe regardless of which level is removed
		self.assertEqual(is_almost_safe([1,3,2,4,5]), True)  # Safe by removing the second level, 3
		self.assertEqual(is_almost_safe([8,6,4,4,1]), True)  # Safe by removing the third level, 4
		self.assertEqual(is_almost_safe([1,3,6,7,9]), True)  # Safe without removing any level


if __name__ == "__main__":
	solve_p1()
	solve_p2()