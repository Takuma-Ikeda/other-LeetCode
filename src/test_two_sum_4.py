import unittest
from answer import two_sum_4


class TestSolution(unittest.TestCase):

    def setUp(self):
        n2 = two_sum_4.TreeNode(2, None, None)
        n4 = two_sum_4.TreeNode(4, None, None)
        n7 = two_sum_4.TreeNode(7, None, None)
        n3 = two_sum_4.TreeNode(3, n2, n4)
        n6 = two_sum_4.TreeNode(6, None, n7)
        n5 = two_sum_4.TreeNode(5, n3, n6)
        self.root = n5
        self.k1 = 9
        self.k2 = 28

    def test_solution1(self):
        s = two_sum_4.Solution()
        result = s.findTarget(self.root, self.k1)
        self.assertTrue(result)

    def test_solution2(self):
        s = two_sum_4.Solution()
        result = s.findTarget(self.root, self.k2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
