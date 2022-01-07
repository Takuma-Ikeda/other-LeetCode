import unittest
from answer.binary_search_tree_to_greater_sum_tree import Solution, TreeNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root = [
            TreeNode(4,
                TreeNode(1,
                    TreeNode(0),
                    TreeNode(2,
                        None,
                        TreeNode(3)
                    )
                ),
                TreeNode(6,
                    TreeNode(5),
                    TreeNode(7,
                        None,
                        TreeNode(8)
                    )
                )
            ),
            TreeNode(0,
                None,
                TreeNode(1)
            )
        ]
        self.answers = [
            TreeNode(30,
                TreeNode(36,
                    TreeNode(36),
                    TreeNode(35,
                        None,
                        TreeNode(33)
                    )
                ),
                TreeNode(21,
                    TreeNode(26),
                    TreeNode(15,
                        None,
                        TreeNode(8)
                    )
                )
            ),
            TreeNode(1,
                None,
                TreeNode(1)
            )
        ]

    def test_solution(self):
        def recur(root, answer):
            if root.val:
                self.assertEqual(root.val, answer.val)

            if root.left:
                recur(root.left, answer.left)

            if root.right:
                recur(root.right, answer.right)

        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            root = s.bstToGst(self.root[i])
            recur(root, self.answers[i])


if __name__ == "__main__":
    unittest.main()
