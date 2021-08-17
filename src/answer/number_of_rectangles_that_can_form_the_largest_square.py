from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        squares = []

        for r in rectangles:
            length = min(r)
            squares.append(length)
            max_len = length if length > max_len else max_len

        return squares.count(max_len)

# 模範解答
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/discuss/1020928/Python-easier-solution-with-explanation-(dictionary)


'''
class Solution:
    def countGoodRectangles(self, rectangles):
        // 辞書型で key は 長さの数値、value は出現回数を管理する
        t = {}
        for r in rectangles:
            p = min(r)
            if p in t:
                t[p] += 1
            else:
                t[p] = 1
        return t[max(t.keys())]
'''
