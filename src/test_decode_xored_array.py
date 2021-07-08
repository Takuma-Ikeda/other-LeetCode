import unittest
from answer.decode_xored_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.encoded = [
            [1, 2, 3],
            [6, 2, 7, 3],
        ]
        self.first = [
            1,
            4,
        ]
        self.answers = [
            [1, 0, 2, 1],
            [4, 2, 0, 7, 4],
        ]

    def solution(self, i):
        s = Solution()
        result = s.decode(self.encoded[i], self.first[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
