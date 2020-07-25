import unittest
from answer import two_sum_4


class DummyData():
    def __init__(self):
        n2 = two_sum_4.TreeNode(2, None, None)
        n4 = two_sum_4.TreeNode(4, None, None)
        n7 = two_sum_4.TreeNode(7, None, None)
        n3 = two_sum_4.TreeNode(3, n2, n4)
        n6 = two_sum_4.TreeNode(6, None, n7)
        n5 = two_sum_4.TreeNode(5, n3, n6)

        self.treeNode = n5

        self.target1 = 9
        self.answer1 = True

        self.target2 = 28
        self.answer2 = False


class TestSolution(unittest.TestCase):

    def test_solution1(self):
        d = DummyData()
        s = two_sum_4.Solution()
        result = s.findTarget(d.treeNode, d.target1)
        self.assertEqual(d.answer1, result)

    def test_solution2(self):
        d = DummyData()
        s = two_sum_4.Solution()
        result = s.findTarget(d.treeNode, d.target2)
        self.assertEqual(d.answer2, result)


if __name__ == "__main__":
    unittest.main()
