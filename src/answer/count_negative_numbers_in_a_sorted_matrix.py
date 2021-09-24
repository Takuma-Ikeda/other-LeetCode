from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0

        for li in grid:
            # result += sum(v < 0 for v in li) の方がシンプル
            result += sum(1 if v < 0 else 0 for v in li)

        return result


# 模範解答
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/514468/4-Python-Solutions

'''
# O(n^2): 行と列の組み合わせ走査 (Brutal Force)
class Solution:
    def countNegatives(self, grid):
        count = 0

        for i in range(len(grid)-1, -1,-1):
            for j in range(len(grid[0])-1,-1, -1):
                if grid[i][j] < 0:
                    count += 1

        return(count)
'''

'''
# O(n^2): 行と列の組み合わせ走査 (Brutal Force)
class Solution:
    def countNegatives(self, grid):
        return sum(a < 0 for i in grid for a in i)
'''

'''
# O(m + n): 行ごとの走査
class Solution(object):
    def countNegatives(self, grid):
        i = len(grid) - 1
        j = 0
        count = 0

        # 一回のループで全部の組み合わせを見る
        while (i >= 0) and (j < len(grid[0])):
            if grid[i][j] < 0:
                count += len(grid[0]) - j
                i -= 1
            else:
                j += 1

        return(count)
'''

'''
# O(mlogn): バイナリサーチ
class Solution(object):
    def countNegatives(self, grid):
        # 関数内関数
        def bin(row):
            start, end = 0, len(row)

            while start < end:
                mid = start + (end -start) // 2

                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1

            return len(row) - start

        count = 0

        for row in grid:
            count += bin(row)

        return count
'''
