import unittest
from answer.easy.flipping_an_image import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.image = [
            [[1, 1, 0], [1, 0, 1], [0, 0, 0]],
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
        ]
        self.answers = [
            [[1, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        ]

    def solution(self, i):
        s = Solution()
        result = s.flipAndInvertImage(self.image[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
