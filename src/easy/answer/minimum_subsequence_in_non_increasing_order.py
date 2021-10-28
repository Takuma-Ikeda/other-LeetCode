from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        result = []
        desc = sorted(nums, reverse=True)

        for idx, val in enumerate(desc):
            result.append(val)

            if sum(result) > sum(desc[idx + 1:]):
                break

        return result

# 模範解答
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/discuss/662565/Simple-and-Easy-Solution-by-Python-3


'''
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [nums.pop()]

        while sum(result) <= sum(nums):
            result.append(nums.pop())

        return result
'''
