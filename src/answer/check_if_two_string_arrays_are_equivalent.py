from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = str2 = ''

        for w in word1:
            str1 += w

        for w in word2:
            str2 += w

        if str1 == str2:
            return True

        return False

# 模範解答
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/discuss/944697/Python-3-or-Python-1-liner-or-No-explanation


'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # join メソッドを使えば for ... in 構文が不要になる
        return ''.join(word1) == ''.join(word2)
'''
