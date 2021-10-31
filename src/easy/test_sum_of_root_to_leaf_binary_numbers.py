import unittest
from answer.sum_of_root_to_leaf_binary_numbers import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.root = [
            TreeNode(1,
                TreeNode(0, TreeNode(0), TreeNode(1)),
                TreeNode(1, TreeNode(0), TreeNode(1))
            ),
            TreeNode(0),
            TreeNode(1),
            TreeNode(1, TreeNode(1), None)
        ]

        self.answers = [
            22,
            0,
            1,
            3,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.sumRootToLeaf(self.root[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
