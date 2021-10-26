import unittest
from answer.maximum_units_on_a_truck import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.boxTypes = [
            [[1, 3], [2, 2], [3, 1]],
            [[5, 10], [2, 5], [4, 7], [3, 9]],
        ]
        self.truckSize = [
            4,
            10
        ]
        self.answers = [
            8,
            91,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.maximumUnits(self.boxTypes[i], self.truckSize[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
