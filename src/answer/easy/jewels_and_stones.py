class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:

        count = 0

        # いちいち list(J) して回さなくても OK
        for j in J:
            for s in S:
                if j == s:
                    count += 1

        return count

# 模範解答
# https://leetcode.com/problems/jewels-and-stones/discuss/775235/Python-3-greater-99.12-faster.-Simple-solution

# DefaultDict クラスを使う方法
# 参考) https://qiita.com/xza/items/72a1b07fcf64d1f4bdb7


'''
from collections import defaultdict
from typing import DefaultDict


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        # defaultdict(int) 関数で DefaultDict[int] クラス型のハッシュマップ stones を作成
        stones:DefaultDict[int] = defaultdict(int)
        count = 0

        for c in S:
            # 文字の登場回数をカウントする
            stones[c] += 1

        # ここで print(stones) すると、以下のようなハッシュマップが得られる
        # defaultdict(<class 'int'>, {'a': 1, 'A': 2, 'b': 4})
        # defaultdict(<class 'int'>, {'Z': 2})
                    
        for j in J:
            if stones and j in stones:
                count += stones[j]
                
        return count
'''

# Counter クラスを使う方法

'''
from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    
        # Counter クラス型のハッシュマップ stones を作成
        stones = Counter(S)
        count = 0
        
        # ここで print(stones) すると、以下のようなハッシュマップが得られる
        # Counter({'b': 4, 'A': 2, 'a': 1})
        # Counter({'Z': 2})
       
        for j in J:
            if stones and j in stones:
                count += stones[j]
                
        return count
'''
