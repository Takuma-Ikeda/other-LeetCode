import unittest
from answer.easy.increasing_order_search_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.node = [
            TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9)))),
            TreeNode(5, TreeNode(1), TreeNode(7))
        ]
        self.answers = [
            TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, TreeNode(7, None, TreeNode(8, None, TreeNode(9))))))))),
            TreeNode(1, None, TreeNode(5, None, TreeNode(7)))
        ]

    def solution(self, i):
        s = Solution()
        result = s.increasingBST(self.node[i])
        self.assertVal(result, self.answers[i])

    def assertVal(self, result, answer):
        if (result is not None):
            self.assertEqual(result.val, answer.val)
            self.assertVal(result.left, answer.left)
            self.assertVal(result.right, answer.right)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
