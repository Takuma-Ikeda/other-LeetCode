from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        new_items = []
        # 要素が辞書型である List に変換する
        for v in items:
            k = ['type', 'color', 'name']
            new_items += [dict(zip(k, v))]
        # key と value が一致したら result に 1 プラスする
        for item in new_items:
            result += 1 if ((ruleKey, ruleValue) in item.items()) else 0
        return result

# 模範解答
# https://leetcode.com/problems/count-items-matching-a-rule/discuss/1085906/Python-3-or-2-liner-or-Explanation


'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # index 0 が 'type', index 1 が 'color', index 2 が 'name' を表すという意味
        d = {'type': 0, 'color': 1, 'name': 2}
        
        # ジェネレータ型を作成する内包表記
        # if の結果が true であれば 1 を sum するメソッド実行 (変数 result も必要ない)
        return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
'''
