import unittest
from answer.easy.determine_color_of_a_chessboard_square import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.coordinates = [
            'a1',
            'h3',
            'c7',
        ]
        self.answers = [
            False,
            True,
            False,
        ]

    def solution(self, i):
        s = Solution()
        result = s.squareIsWhite(self.coordinates[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
