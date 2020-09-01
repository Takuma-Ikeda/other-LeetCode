from typing import List


class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:

        list_s = list(s)
        d = {}
        count = 0
        result = ''

        for i in indices:
            d[i] = list_s[count]
            count += 1

        for index in range(count):
            result += d[index]

        return result

# 模範解答
# https://leetcode.com/problems/shuffle-string/discuss/755911/Python-3-lines-easy-O(n)


'''
from typing import List

class Solution:
    
    def restoreString(self, s: str, indices: List[int]) -> str:
    
        # 以下のような、要素が「空文字」のリストで初期化する
        # ['', '', '', '', '', '', '', '']
        res = [''] * len(s)
        
        # 文字列を 1 文字ずつ処理する ※ index 付き
        for index, char in enumerate(s):
            # 空文字を上書きする
            res[indices[index]] = char
            
        # リスト要素を全部くっつけて「文字列」にしてしまう
        return "".join(res)
'''
