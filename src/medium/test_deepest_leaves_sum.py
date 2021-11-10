import unittest
from answer.deepest_leaves_sum import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root = [
            TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7), None), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8)))),
            TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9), None), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1, None, None), TreeNode(3, None, TreeNode(5))))
        ]
        self.answers = [
            15,
            19,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.deepestLeavesSum(self.root[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
