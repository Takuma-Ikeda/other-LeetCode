from typing import List


class Solution:

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for i in range(len(accounts)):
            total = 0
            for num in accounts[i]:
                total += num
            result = total if (total > result) else result
        return result

# 模範解答
# https://leetcode.com/problems/richest-customer-wealth/discuss/955815/Python-one-liner-with-max-and-map-44-ms-14.2-MB


'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # map: ジェネレータ関数。第二引数の要素を取り出して、第一引数の関数 sum に渡して計算する、計算結果をリストで返却する
        # max: リスト要素の最大値のみ返却する
        return max(map(sum, accounts))
'''
