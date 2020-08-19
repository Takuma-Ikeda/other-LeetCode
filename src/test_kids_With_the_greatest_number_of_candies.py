import unittest
from answer.kids_With_the_greatest_number_of_candies import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.candies = [
            [2, 3, 5, 1, 3],
            [4, 2, 1, 1, 2],
            [12, 1, 12]
        ]
        self.extraCandies = [
            3,
            1,
            10
        ]
        self.answers = [
            [True, True, True, False, True],
            [True, False, False, False, False],
            [True, False, True],
        ]

    def solution(self, i):
        s = Solution()
        result = s.kidsWithCandies(self.candies[i], self.extraCandies[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
