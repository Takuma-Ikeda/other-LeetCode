import unittest
from answer.maximum_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [3, 2, 1, 6, 0, 5],
            [3, 2, 1],
        ]
        self.answers = [
            TreeNode(6, TreeNode(3, None, TreeNode(2, None, TreeNode(1))), TreeNode(5, TreeNode(0), None)),
            TreeNode(3, None, TreeNode(2, None, TreeNode(1)))
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.constructMaximumBinaryTree(self.nums[i])

            def recur(result, answer):
                self.assertEqual(answer.val, result.val)

                if answer.left:
                    recur(result.left, answer.left)

                if answer.right:
                    recur(result.right, answer.right)

            recur(result, self.answers[i])


if __name__ == "__main__":
    unittest.main()
