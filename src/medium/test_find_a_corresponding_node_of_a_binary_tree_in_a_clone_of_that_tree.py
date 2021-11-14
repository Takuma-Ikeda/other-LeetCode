import unittest
from answer.find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.target = [
            TreeNode(3,
                TreeNode(6),
                TreeNode(19)
            ),
            TreeNode(7),
            TreeNode(4, None,
                TreeNode(3, None,
                    TreeNode(2, None,
                        TreeNode(1)
                    )
                )
            ),
            TreeNode(5,
                TreeNode(10),
                None
            ),
            TreeNode(2,
                TreeNode(3)
            ),
        ]
        self.answers = [
            TreeNode(3,
                TreeNode(6),
                TreeNode(19)
            ),
            TreeNode(7),
            TreeNode(4, None,
                TreeNode(3, None,
                    TreeNode(2, None,
                        TreeNode(1)
                    )
                )
            ),
            TreeNode(5,
                TreeNode(10),
                None
            ),
            TreeNode(2,
                TreeNode(3)
            ),
        ]
        self.original = [
            TreeNode(7,
                TreeNode(4),
                self.target[0],
            ),
            self.target[1],
            TreeNode(8, None,
                TreeNode(6, None,
                    TreeNode(5, None,
                        self.target[2],
                    )
                )
            ),
            TreeNode(1,
                TreeNode(2,
                    TreeNode(4,
                        TreeNode(8),
                        TreeNode(9)
                    ),
                    self.target[3],
                ),
                TreeNode(3,
                    TreeNode(6),
                    TreeNode(7)
                )
            ),
            TreeNode(1,
                self.target[4],
            ),
        ]
        self.cloned = [
            TreeNode(7,
                TreeNode(4),
                self.answers[0],
            ),
            self.answers[1],
            TreeNode(8, None,
                TreeNode(6, None,
                    TreeNode(5, None,
                        self.answers[2],
                    )
                )
            ),
            TreeNode(1,
                TreeNode(2,
                    TreeNode(4,
                        TreeNode(8),
                        TreeNode(9)
                    ),
                    self.answers[3],
                ),
                TreeNode(3,
                    TreeNode(6),
                    TreeNode(7)
                )
            ),
            TreeNode(1,
                self.answers[4],
            ),
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.getTargetCopy(self.original[i], self.cloned[i], self.target[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
