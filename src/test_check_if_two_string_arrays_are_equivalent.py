import unittest
from answer.easy.check_if_two_string_arrays_are_equivalent import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.word1 = [
           ['ab', 'c'],
           ['a', 'cb'],
           ['abc', 'd', 'defg'],
        ]
        self.word2 = [
           ['a', 'bc'],
           ['ab', 'c'],
           ['abcddefg'],
        ]
        self.answers = [
            True,
            False,
            True,
        ]

    def solution(self, i):
        s = Solution()
        result = s.arrayStringsAreEqual(self.word1[i], self.word2[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
