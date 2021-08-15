from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            # flip
            i.reverse()

            # invert
            for index, val in enumerate(i):
                i[index] = 1 if val == 0 else 0
        return image

# 模範解答
# https://leetcode.com/problems/flipping-an-image/discuss/550889/The-Python3-One-Liner


'''
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # スライス [::-1] は要素が逆順になる
        return [[0 if v == 1 else 1 for v in x][::-1] for x in image]
'''
