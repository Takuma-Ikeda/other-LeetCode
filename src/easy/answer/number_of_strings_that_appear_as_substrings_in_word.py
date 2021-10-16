from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # return sum(x in word for x in patterns) でよい
        return sum(1 for p in patterns if p in word)

# 模範解答
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/discuss/1404073/Python3-1-line


'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(x in word for x in patterns)
'''
