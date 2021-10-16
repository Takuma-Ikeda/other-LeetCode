from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        cells = []
        count = 0

        # init
        for _ in range(m):
            element = []
            for _ in range(n):
                element.append(0)
            cells.append(element)

        # indices[n][0] を row, indices[n][1] を col として取り出す
        for row, col in indices:
            # row increment
            for i, v in enumerate(cells[row]):
                cells[row][i] = v + 1

            # col increment
            for cell in cells:
                cell[col] = cell[col] + 1

        # count odd number
        for cell in cells:
            count += sum(1 for v in cell if v % 2 == 1)

        return count

# 模範解答
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/discuss/425117/Python-3-(With-Explanation)-(five-lines)-(48-ms)


'''
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # 要素 0 で初期化
        M = [[0] * m for _ in range(n)]

        for x, y in indices:
            for j in range(m):
                M[x][j] = 1 - M[x][j]

            for i in range(n):
                M[i][y] = 1 - M[i][y]

        return sum(sum(M, []))
'''
