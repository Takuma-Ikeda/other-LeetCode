import unittest
from answer.easy.count_good_triplets import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr = [
            [3, 0, 1, 1, 9, 7],
            [1, 1, 2, 2, 3],
        ]
        self.a = [
            7,
            0,
        ]
        self.b = [
            2,
            0,
        ]
        self.c = [
            3,
            1,
        ]
        self.answer = [
            4,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.countGoodTriplets(self.arr[i], self.a[i], self.b[i], self.c[i])
        self.assertEqual(result, self.answer[i])

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
