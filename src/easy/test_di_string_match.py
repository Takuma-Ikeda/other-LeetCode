import unittest
from answer.di_string_match import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            'IDID',
            'III',
            'DDI',
        ]
        self.answers = [
            [0, 4, 1, 3, 2],
            [0, 1, 2, 3],
            [3, 2, 0, 1],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.diStringMatch(self.s[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()

