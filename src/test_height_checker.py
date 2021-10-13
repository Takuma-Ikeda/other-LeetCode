import unittest
from answer.height_checker import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.heights = [
            [1, 1, 4, 2, 1, 3],
            [5, 1, 2, 3, 4],
            [1, 2, 3, 4, 5],
        ]
        self.answers = [
            3,
            5,
            0,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.heightChecker(self.heights[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()


# 模範解答
# https://leetcode.com/problems/height-checker/discuss/476062/Python-O(n)-solution-Counting-sort

'''
from collections import Counter


class Solution:
    def heightChecker(self, heights):
        i = 0
        removals = 0
        counter = Counter(heights)

        # 分布数え上げソート: Counting Sort
        # https://www.codereading.com/algo_and_ds/algo/counting_sort.html
        for height in heights:
            while counter[i] == 0:
                i += 1

            if i != height:
                removals += 1

            counter[i] -= 1

        return removals
'''
