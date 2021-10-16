
import unittest
from answer.easy.number_of_students_doing_homework_at_a_given_time import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.startTime = [
            [1, 2, 3],
            [4],
            [4],
            [1, 1, 1, 1],
            [9, 8, 7, 6, 5, 4, 3, 2, 1],
        ]
        self.endTime = [
            [3, 2, 7],
            [4],
            [4],
            [1, 3, 2, 4],
            [10, 10, 10, 10, 10, 10, 10, 10, 10]
        ]
        self.queryTime = [
            4,
            4,
            5,
            7,
            5,
        ]
        self.answers = [
            1,
            1,
            0,
            0,
            5,
        ]

    def solution(self, i):
        s = Solution()
        result = s.busyStudent(self.startTime[i], self.endTime[i], self.queryTime[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)

    def test_solution4(self):
        self.solution(4)


if __name__ == "__main__":
    unittest.main()
