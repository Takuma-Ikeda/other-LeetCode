import unittest
from answer.find_center_of_star_graph import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [[1, 2], [2, 3], [4, 2]],
            [[1, 2], [5, 1], [1, 3], [1, 4]],
        ]
        self.answers = [
            2,
            1,
        ]

    def solution(self, i):
        s = Solution()
        result = s.findCenter(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
