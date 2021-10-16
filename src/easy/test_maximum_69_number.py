import unittest
from answer.maximum_69_number import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            9669,
            9996,
            9999,
        ]
        self.answers = [
            9969,
            9999,
            9999,
        ]

    def solution(self, i):
        s = Solution()
        result = s.maximum69Number(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
