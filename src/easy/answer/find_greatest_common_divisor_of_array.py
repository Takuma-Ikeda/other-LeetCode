from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        for i in range(smallest, 0, -1):
            if (largest % i == 0) and (smallest % i == 0):
                return i

# 模範解答
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/discuss/1422287/Euclidean-GCD-3-line-python


'''
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m, n = max(nums), min(nums)

        # ユークリッド距離
        while n:
            m, n = n, m % n
        return m
'''
