import unittest
from answer.find_n_unique_integers_sum_up_to_zero import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.n = [
            5,
            3,
            1,
        ]

    def solution(self, i):
        s = Solution()
        result = s.sumZero(self.n[i])

        # 重複チェック
        self.assertTrue(len(result) == len(set(result)))

        # 足し算して 0 になるかチェック
        count = 0
        for v in result:
            count += v

        self.assertEqual(count, 0)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
