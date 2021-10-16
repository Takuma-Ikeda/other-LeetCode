from typing import List
from collections import defaultdict


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for v in nums:
            d[v] += 1

        for k, v in d.items():
            if v > 1:
                return k

# 模範解答
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/551278/Use-count()-or-Python3-or-Super-Easy!


'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for v in nums:
            # count: 値を指定して、その値の要素がいくつ存在するか取得できる
            if nums.count(v) > 1:
                return x
'''

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/574042/Python-1-liner-using-mode

'''
# from statistics import mode


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # 最頻値を取得する
        return mode(nums)
'''

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/382179/Three-Solutions-in-Python-3

'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return (lambda x: max(x, key = lambda y: x[y]))(collections.Counter(nums))
'''

'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        S = set()
        for a in nums:
            if a in S: return a
            else: S.add(a)
'''

'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for a in set(nums):
            if nums.count(a) != 1: return a
'''
