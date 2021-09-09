class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = dict()

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        first = True
        number = 0

        for _, val in d.items():
            if first:
                number = val
                first = False
            else:
                if number != val:
                    return False

        return True

# 模範解答
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/discuss/1359715/Python3-1-line


'''
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Counter クラスで文字列・リスト要素の文字出現回数をカウントしたハッシュマップを作成できる
        # 出現回数の数値で「集合型」を作成
        # 重複がなければ集合要素は 1 つだけである
        return len(set(Counter(s).values())) == 1
'''
