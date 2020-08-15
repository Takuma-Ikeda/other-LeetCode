import unittest
from answer import two_sum_2


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
        s = two_sum_2.Solution()
        result = s.twoSum(self.numbers[i], self.targets[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        self.solution(0)


if __name__ == "__main__":
    unittest.main()

