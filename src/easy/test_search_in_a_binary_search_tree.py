import unittest
from answer.search_in_a_binary_search_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.root = [
            TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)),
            TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)),
        ]
        self.val = [
            2,
            5,
        ]
        self.answers = [
            TreeNode(2, TreeNode(1), TreeNode(3)),
            None,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.searchBST(self.root[i], self.val[i])

            if self.answers[i] is None:
                self.assertEqual(self.answers[i], result)
            else:
                self.assertEqual(self.getNodeVals(self.answers[i]), self.getNodeVals(result))

    def getNodeVals(self, root):
        result = []

        def search(root):
            result.append(root.val)

            if root.left is not None:
                search(root.left)

            if root.right is not None:
                search(root.right)

        search(root)
        return result


if __name__ == "__main__":
    unittest.main()
