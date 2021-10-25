import unittest
from answer.unique_number_of_occurrences import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr = [
            [1, 2, 2, 1, 1, 3],
            [1, 2],
            [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
        ]
        self.answers = [
            True,
            False,
            True,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.uniqueOccurrences(self.arr[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
