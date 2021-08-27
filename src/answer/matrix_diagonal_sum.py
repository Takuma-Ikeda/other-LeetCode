from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        h = w = len(mat)
        result = 0

        # primary diagonal
        j = 0
        for i in range(h):
            result += mat[i][j]
            j += 1

        # secondary diagonal
        j = len(mat) - 1
        for i in range(h):
            result += mat[i][j]
            j -= 1

        # マトリクスの幅が奇数のときだけ、中央の要素が重複しているのでマイナスする
        if not (w % 2 == 0):
            i = w // 2
            result -= mat[i][i]

        return result

# 模範解答
# https://leetcode.com/problems/matrix-diagonal-sum/discuss/837795/Python-O(n)-by-iteration-w-Comment


'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid = n // 2
        summation = 0

        for i in range(n):
            # primary diagonal
            summation += mat[i][i]

            # secondary diagonal
            summation += mat[n-1-i][i]

        if n % 2 == 1:
            summation -= mat[mid][mid]

        return summation
'''
