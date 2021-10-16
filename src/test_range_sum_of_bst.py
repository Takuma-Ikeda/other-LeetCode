import unittest
from answer.easy.range_sum_of_bst import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root = [
            TreeNode(
                10,
                TreeNode(5, TreeNode(3, None, None), TreeNode(7, None, None)),
                TreeNode(15, None, TreeNode(18, None, None))
            ),
            TreeNode(
                10,
                TreeNode(5, TreeNode(3, TreeNode(1, None, None), None), TreeNode(7, TreeNode(6, None, None), None)),
                TreeNode(15, TreeNode(13, None, None), TreeNode(18, None, None))
            ),
        ]
        self.low = [
            7,
            6,
        ]
        self.high = [
            15,
            10,
        ]
        self.answers = [
            32,
            23,
        ]

    def solution(self, i):
        s = Solution()
        return s.rangeSumBST(self.root[i], self.low[i], self.high[i])

    def test_solution0(self):
        result = self.solution(0)
        self.assertEqual(result, self.answers[0])

    def test_solution1(self):
        result = self.solution(1)
        self.assertEqual(result, self.answers[1])


if __name__ == "__main__":
    unittest.main()
