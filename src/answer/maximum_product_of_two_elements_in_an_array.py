from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v1 = max(nums)
        del nums[nums.index(v1)]

        v2 = max(nums)
        del nums[nums.index(v2)]

        return (v1 - 1) * (v2 - 1)


# 模範解答
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/discuss/662754/Python-Built-in-sort-method-(100-speed-100-mem)


'''
class Solution(object):
    def maxProduct(self, nums):
        # 昇順ソートして、末尾・末尾からひとつ手前の要素で演算する
        nums.sort()
        return (nums[-1] -1) * (nums[-2] - 1)
'''
