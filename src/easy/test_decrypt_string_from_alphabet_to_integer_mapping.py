import unittest
from answer.decrypt_string_from_alphabet_to_integer_mapping import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            "10#11#12",
            "1326#",
            "25#",
            "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#",
        ]
        self.answers = [
            "jkab",
            "acz",
            "y",
            "abcdefghijklmnopqrstuvwxyz",
        ]

    def solution(self, i):
        s = Solution()
        result = s.freqAlphabets(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)


if __name__ == "__main__":
    unittest.main()
