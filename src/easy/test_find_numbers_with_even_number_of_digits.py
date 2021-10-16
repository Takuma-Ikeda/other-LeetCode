import unittest
from answer.find_numbers_with_even_number_of_digits import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [12, 345, 2, 6, 7896],
            [555, 901, 482, 1771]
        ]
        self.answers = [
            2,
            1,
        ]

    def solution(self, i):
        s = Solution()
        result = s.findNumbers(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
