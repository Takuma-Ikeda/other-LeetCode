import unittest
from answer.sum_of_nodes_with_even_valued_grandparent import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root = [
            TreeNode(6,
                TreeNode(7,
                    TreeNode(2,
                        TreeNode(9),
                        None),
                    TreeNode(7,
                        TreeNode(1),
                        TreeNode(4)
                    )
                ),
                TreeNode(8,
                    TreeNode(1),
                    TreeNode(3,
                        None,
                        TreeNode(5)
                    )
                )
            ),
            TreeNode(1)
        ]
        self.answers = [
            18,
            0,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.sumEvenGrandparent(self.root[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
