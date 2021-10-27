from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result, soldiers, tmp = [], [], []

        [soldiers.append(m.count(1)) for m in mat]
        tmp = soldiers

        while tmp:
            # 最小値の index を取得
            indices = [i for i, v in enumerate(soldiers) if v == min(tmp)]
            result.extend(indices)
            # 現在の最小値を削除
            tmp = [v for v in tmp if v != min(tmp)]

            if len(result) >= k:
                break

        return result[0:k]

# 模範解答
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/496644/Clean-Python-3-beats-100-without-sort-or-heap


'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = {}

        for j in range(n):
            for i in range(m):
                if mat[i][j] or i in result:
                    continue

                result[i] = True
                k -= 1

                if not k:
                    return result.keys()

        for i in range(m):
            if i not in result:
                result[i] = True
                k -= 1

                if not k:
                    return result.keys()
'''
