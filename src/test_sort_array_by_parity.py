import unittest
from answer.sort_array_by_parity import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [3, 1, 2, 4],
            [0],
        ]
        self.answers = [
            [2, 4, 3, 1],
            [0],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.sortArrayByParity(self.nums[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()


# 模範解答
# https://leetcode.com/problems/sort-array-by-parity/discuss/356271/Solution-in-Python-3-(beats-~96)-(short)-(-O(1)-space-)-(-O(n)-speed-)

'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            if (nums[i] % 2 == 1) and (nums[j] % 2 == 0):
                nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1 - nums[i] % 2, j - nums[j] % 2

        return nums
'''

'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x : x % 2)
'''

'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [i for i in nums if not i % 2] + [i for i in nums if i % 2]
'''
