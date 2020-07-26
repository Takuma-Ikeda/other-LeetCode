import unittest
from answer import two_sum_2


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.numbers = [2, 7, 11, 15]
        self.target = 9
        self.answer = [1, 2]

    def test_solution1(self):
        s = two_sum_2.Solution()
        result = s.twoSum(self.numbers, self.target)
        self.assertEqual(self.answer, result)


if __name__ == "__main__":
    unittest.main()

