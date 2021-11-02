import unittest
from answer.partitioning_into_minimum_number_of_deci_binary_numbers import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.n = [
            '32',
            '82734',
            '27346209830709182346',
        ]
        self.answers = [
            3,
            8,
            9,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.minPartitions(self.n[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
