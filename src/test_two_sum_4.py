import unittest
from answer.two_sum_4 import Solution, TreeNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        n2 = TreeNode(2, None, None)
        n4 = TreeNode(4, None, None)
        n7 = TreeNode(7, None, None)
        n3 = TreeNode(3, n2, n4)
        n6 = TreeNode(6, None, n7)
        self.root = TreeNode(5, n3, n6)
        self.ks = [
            9,
            28
        ]

    def solution(self, i):
        s = Solution()
        return s.findTarget(self.root, self.ks[i])

    def test_solution(self):
        result = self.solution(0)
        self.assertTrue(result)

    def test_solution1(self):
        result = self.solution(1)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
