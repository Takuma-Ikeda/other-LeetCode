import unittest
from answer.execution_of_all_suffix_instructions_staying_in_a_grid import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.n = [
            3,
            2,
            1,
        ]
        self.startPos = [
            [0, 1],
            [1, 1],
            [0, 0],
        ]
        self.s = [
            'RRDDLU',
            'LURD',
            'LRUD',
        ]
        self.answers = [
            [1, 5, 4, 3, 1, 0],
            [4, 1, 0, 0],
            [0, 0, 0, 0],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.executeInstructions(self.n[i], self.startPos[i], self.s[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
