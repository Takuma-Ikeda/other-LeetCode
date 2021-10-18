import unittest
from answer.check_if_numbers_are_ascending_in_a_sentence import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            "1 box has 3 blue 4 red 6 green and 12 yellow marbles",
            "hello world 5 x 5",
            "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s",
            "4 5 11 26",
        ]
        self.answers = [
            True,
            False,
            False,
            True,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.areNumbersAscending(self.s[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
