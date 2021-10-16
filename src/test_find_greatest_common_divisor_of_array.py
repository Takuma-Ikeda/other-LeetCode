import unittest
from answer.easy.find_greatest_common_divisor_of_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [2, 5, 6, 9, 10],
            [7, 5, 6, 8, 3],
            [3, 3],
        ]

        self.answers = [
            2,
            1,
            3,
        ]

    def solution(self, i):
        s = Solution()
        result = s.findGCD(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
