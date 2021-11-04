import unittest
from answer.minimum_number_of_operations_to_move_all_balls_to_each_box import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.boxes = [
            '110',
            '001011',
        ]
        self.answers = [
            [1, 1, 3],
            [11, 8, 5, 4, 3, 4],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.minOperations(self.boxes[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
