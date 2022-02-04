from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = device = 0

        for v in bank:
            beams += device * v.count("1")

            if v.count("1") > 0:
                device = v.count("1")

        return beams

# 模範解答
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/discuss/1660943/Python3-Java-C%2B%2B-Simple-O(mn)


'''
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0

        for s in bank:
            c = s.count('1')

            if c:
                ans += prev * c
                prev = c

        return ans
'''
