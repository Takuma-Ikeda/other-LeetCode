import unittest
from answer.make_two_arrays_equal_by_reversing_sub_arrays import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.target = [
            [1, 2, 3, 4],
            [7],
            [1, 12],
            [3, 7, 9],
            [1, 1, 1, 1, 1],
        ]
        self.arr = [
            [2, 4, 1, 3],
            [7],
            [12, 1],
            [3, 7, 11],
            [1, 1, 1, 1, 1],
        ]
        self.answers = [
            True,
            True,
            True,
            False,
            True,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.canBeEqual(self.target[i], self.arr[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
