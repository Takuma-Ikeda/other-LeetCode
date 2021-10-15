import unittest
from answer.minimum_time_to_type_word_using_special_typewriter import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.word = [
            'abc',
            'bza',
        ]
        self.answers = [
            5,
            7,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.minTimeToType(self.word[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
