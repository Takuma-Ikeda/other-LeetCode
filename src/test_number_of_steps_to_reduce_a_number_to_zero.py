import unittest
from answer.number_of_steps_to_reduce_a_number_to_zero import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            14,
            8,
            123
        ]
        self.answers = [
            6,
            4,
            12
        ]

    def solution(self, i):
        s = Solution()
        result = s.numberOfSteps(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
