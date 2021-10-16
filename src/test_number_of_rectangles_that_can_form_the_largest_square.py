import unittest
from answer.easy.number_of_rectangles_that_can_form_the_largest_square import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.rectangles = [
            [[5, 8], [3, 9], [5, 12], [16, 5]],
            [[2, 3], [3, 7], [4, 3], [3, 7]],
        ]
        self.answers = [
            3,
            3,
        ]

    def solution(self, i):
        s = Solution()
        result = s.countGoodRectangles(self.rectangles[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
