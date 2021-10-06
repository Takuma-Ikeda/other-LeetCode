from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0

        # 昇順にして前から組み合わせを作るだけ
        s = sorted(nums)
        i = iter(s)

        for v1, v2 in zip(i, i):
            result += v1 if (v1 < v2) else v2

        return result


# 模範解答
# https://leetcode.com/problems/array-partition-i/discuss/390198/Algorithm-and-solution-in-python3

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0

        for i in range(0, len(nums), 2):
            # 偶数の index 値だけ足し算すればよい
            sum += nums[i]

        return sum
'''

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
'''
