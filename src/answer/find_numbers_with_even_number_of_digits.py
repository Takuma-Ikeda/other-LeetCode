from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for i in nums if len(str(i)) % 2 == 0)

# 模範解答
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/discuss/468107/Python-3-lightning-fast-one-line-solution


'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # 要素を抽出してカウントするパターン
        return len([x for x in nums if len(str(x)) % 2 == 0])
'''
