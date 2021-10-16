import unittest
from answer.easy.two_sum_ii_input_array_is_sorted import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.numbers = [
            [2, 7, 11, 15]
        ]
        self.targets = [
            9
        ]
        self.answers = [
            [1, 2]
        ]

    def solution(self, i):
        s = Solution()
        result = s.twoSum(self.numbers[i], self.targets[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)


if __name__ == "__main__":
    unittest.main()

