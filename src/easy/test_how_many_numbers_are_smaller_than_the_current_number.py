import unittest
from answer.how_many_numbers_are_smaller_than_the_current_number import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [8, 1, 2, 2, 3],
            [6, 5, 4, 8],
            [7, 7, 7, 7]
        ]
        self.answers = [
            [4, 0, 1, 1, 3],
            [2, 1, 0, 3],
            [0, 0, 0, 0]
        ]

    def solution(self, i):
        s = Solution()
        result = s.smallerNumbersThanCurrent(self.nums[i])
        self.assertEqual(self.answers[i], result)
    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
