from typing import List
from itertools import product

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col_len = len(grid)
        row_len = len(grid[0])

        row_max = [max(r) for r in grid]

        # 「*変数」とすると外側のリスト [] が外れる: アンパック
        # https://python.keicode.com/lang/list-unpack-asterisk.php
        col_max = [max(c) for c in zip(*grid)]

        # 行列の個数だけループする
        # (現在の列の最小値 or 現在の行の最小値) - 現在の値
        return sum(min(row_max[i], col_max[j]) - grid[i][j] for i, j in product(range(col_len), range(row_len)))
