import unittest
from answer import two_sum


class DummyData():
    def __init__(self):
        self.data = [2, 7, 11, 15]
        self.target = 9
        self.answer = [0, 1]


class TestSolution(unittest.TestCase):

    def test_solution1(self):
        d = DummyData()
        s = two_sum.Solution()
        result = s.twoSum(d.data, d.target)
        self.assertEqual(d.answer, result)


if __name__ == "__main__":
    unittest.main()
