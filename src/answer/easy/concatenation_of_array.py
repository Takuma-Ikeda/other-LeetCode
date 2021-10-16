from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < 2:
            for num in nums:
                ans += [num]
            i += 1
        return ans

# 模範解答
# https://leetcode.com/problems/concatenation-of-array/discuss/1331744/Python-and-C%2B%2B-Easy-Solutions-Multiple-Approaches-with-O(N)


'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums.append(nums[i])
        return nums
'''

'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # これだけでも List は結合される
        return nums+nums
'''
