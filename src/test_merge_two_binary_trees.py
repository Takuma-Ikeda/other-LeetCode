import unittest
from answer.easy.merge_two_binary_trees import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root1 = [
            TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2, None, None)),
            TreeNode(1),
        ]
        self.root2 = [
            TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))),
            TreeNode(1, TreeNode(2), None),

        ]
        self.answers = [
            TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(4)), TreeNode(5, None, TreeNode(7))),
            TreeNode(2, TreeNode(2), None),
        ]

    def solution(self, i):
        s = Solution()
        result = s.mergeTrees(self.root1[i], self.root2[i])
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
