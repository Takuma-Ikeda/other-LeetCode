from typing import List
from collections import defaultdict


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        d = defaultdict(int)

        for idx, val in enumerate(boxes):
            d[idx] = int(val)

        for idx1 in d:
            operation = 0

            for idx2, val2 in d.items():
                if (idx1 != idx2) and (val2 != 0):
                    operation += abs(idx2 - idx1) * val2

            result.append(operation)

        return result

# 模範解答
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/discuss/1075895/Easy-Python-beats-100-time-and-space


'''
# すべてのボックスを一箇所に移動するためのコスト
    # すべての左ボックスをそこに移動するためのコスト leftCost と
    # すべての右ボックスをそこに移動するためのコスト rightCost の合計
# すべてのインデックスの leftCost は左から右へのシングルパスを使うことで計算できる
# すべてのインデックスの rightCost は右から左へのシングルパスを使うことで計算できる
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)

        for i in range(1, n):
            if boxes[i - 1] == '1':
                leftCount += 1

            leftCost += leftCount
            ans[i] = leftCost

        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                rightCount += 1

            rightCost += rightCount
            ans[i] += rightCost

        return ans
'''
