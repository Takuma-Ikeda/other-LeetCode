import unittest
from answer.final_value_of_variable_after_performing_operations import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.operations = [
            ["--X", "X++", "X++"],
            ["++X", "++X", "X++"],
            ["X++", "++X", "--X", "X--"]
        ]

        self.answers = [
            1,
            3,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.finalValueAfterOperations(self.operations[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
