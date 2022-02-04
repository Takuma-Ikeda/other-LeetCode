import unittest
from answer.number_of_laser_beams_in_a_bank import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.bank = [
            ["011001", "000000", "010100", "001000"],
            ["000", "111", "000"],
        ]
        self.answers = [
            8,
            0,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.numberOfBeams(self.bank[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
