from typing import List
from copy import copy


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []

        while s:
            num = 0
            pos = copy(startPos)

            for c in s:
                if c == 'L':
                    pos[1] += -1
                elif c == 'R':
                    pos[1] += 1
                elif c == 'U':
                    pos[0] += -1
                elif c == 'D':
                    pos[0] += 1

                if not ((0 <= pos[0] < n) and (0 <= pos[1] < n)):
                    break

                num += 1

            result.append(num)
            s = s[1:]

        return result


# 模範解答
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/discuss/1695189/Python-O(m2)-using-imaginary-numbers

'''
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # 数値の末尾に j を付けると「虚数」として扱うことができる
        # 実部を取得 real 属性
        # 虚部を取得 imag 属性

        d = dict(U = -1, D = 1, L = -1j, R = 1j)

        start = startPos[0] + (1j * startPos[1])
        l = len(s)
        result = [0] * l

        for i in range(l):
            pos = start

            for j in range(i, l):
                pos += d[s[j]]

                if not ((0 <= pos.real < n) and (0 <= pos.imag < n)):
                    break

                result[i] += 1

        return result
'''
