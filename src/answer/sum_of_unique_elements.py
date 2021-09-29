from typing import List
from collections import defaultdict


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        d = defaultdict(int)

        for v in nums:
            d[v] += 1

        for k, v in d.items():
            if v == 1:
                result += k

        return result


# 模範解答
# https://leetcode.com/problems/sum-of-unique-elements/discuss/1135187/Python-faster-than-99-(so-they-say)

'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq = []
        [uniq.append(num) for num in nums if nums.count(num) == 1]
        return sum(uniq)
'''
