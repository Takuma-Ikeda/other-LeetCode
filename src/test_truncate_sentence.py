import unittest
from answer.truncate_sentence import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            "Hello how are you Contestant",
            "What is the solution to this problem",
            "chopper is not a tanuki",
        ]
        self.k = [
            4,
            4,
            5,
        ]
        self.answers = [
            "Hello how are you",
            "What is the solution",
            "chopper is not a tanuki",
        ]

    def solution(self, i):
        s = Solution()
        result = s.truncateSentence(self.s[i], self.k[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
