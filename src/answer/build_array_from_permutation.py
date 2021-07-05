from typing import List


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for index in nums:
            ans += [nums[index]]
        return ans

# 模範解答
# https://leetcode.com/problems/build-array-from-permutation/discuss/1314345/Python3-1-line


'''
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 内包表記を利用
        return [nums[nums[i]] for i in range(len(nums))]
'''
