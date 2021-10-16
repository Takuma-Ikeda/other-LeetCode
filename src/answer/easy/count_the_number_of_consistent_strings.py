from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            isConsistent = True

            for char in word:
                if char not in allowed:
                    isConsistent = False

            if isConsistent:
                count += 1

        return count

# 模範解答
# https://leetcode.com/problems/count-the-number-of-consistent-strings/discuss/971323/Python-3-solution-100-faster-than-any-other-codes


'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # 集合型に変換する
        allowed = set(allowed)
        count = 0

        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break

        return len(words) - count
'''
