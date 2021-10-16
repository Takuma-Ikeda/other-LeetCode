import unittest
from answer.easy.destination_city import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.paths = [
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
            [["B", "C"], ["D", "B"], ["C", "A"]],
            [["A", "Z"]],
        ]
        self.answers = [
            "Sao Paulo",
            "A",
            "Z",
        ]

    def solution(self, i):
        s = Solution()
        result = s.destCity(self.paths[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
