from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 出現回数のハッシュマップを作成
        d = Counter(arr)

        # 出現回数で集合型をつくる
        s = set(d.values())

        return len(d) == len(s)

# 模範解答
# https://leetcode.com/problems/unique-number-of-occurrences/discuss/393086/Solution-in-Python-3-(one-line)-(beats-100.00-)


'''
class Solution:
    def uniqueOccurrences(self, A: List[int]) -> bool:
        return (lambda x: len(x) == len(set(x)))(collections.Counter(A).values())
'''

# https://leetcode.com/problems/unique-number-of-occurrences/discuss/458512/Easy-python-solution

'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = []
        set_arr = set(arr)

        for item in set_arr:
            occur.append(arr.count(item))

        return len(occur) == len(set(occur))
'''
