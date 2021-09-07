import unittest
from answer.generate_a_string_with_characters_that_have_odd_counts import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.n = [
            4,
            2,
            7,
        ]

    def solution(self, i):
        s = Solution()
        result = s.generateTheString(self.n[i])

        d = dict()
        for s in result:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

        for _, v in d.items():
            self.assertTrue(v % 2 == 1)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
