import unittest
from answer.decompress_run_length_encoded_list import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 3, 4],
            [1, 1, 2, 3],
        ]
        self.answers = [
            [2, 4, 4, 4],
            [1, 3, 3],
        ]

    def solution(self, i):
        s = Solution()
        result = s.decompressRLElist(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
