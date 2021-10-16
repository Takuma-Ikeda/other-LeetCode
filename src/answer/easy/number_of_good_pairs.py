from typing import List


class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:

        result = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    result += 1
        return result

# 模範解答
# https://leetcode.com/problems/number-of-good-pairs/discuss/736565/Python-Simple-O(n)-Solution


'''
class Solution:
    
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # 要素の繰り返し回数を格納する辞書型 (ハッシュテーブル)        
        repeat = {}
        
        # ペアの総数を記録する
        num = 0
        
        # ループが 1 回で済む方法: 計算量 O(n)
        for v in nums:
            # 値 v の登場が 2 回目以降の場合
            if v in repeat:
                # 初めてペア成立したとき
                if repeat[v] == 1:
                    num += 1
                # 複数回ペア成立したとき
                else:
                    # ペア数は「値の登場回数 + 前回ペア数」で求めることができる
                    num += repeat[v]
                # 値の登場回数 1 増やす
                repeat[v] += 1
            # 値 v の登場が初めての場合
            else:
                # 値の登場回数 1 設定
                repeat[v] = 1

        return num
'''

# ハッシュテーブル解説
# https://suwaru.tokyo/%e3%80%90%e3%82%a8%e3%83%b3%e3%82%b8%e3%83%8b%e3%82%a2%e9%9d%a2%e6%8e%a5%e3%80%91%e6%96%87%e5%ad%97%e5%88%97%e3%83%bb%e9%85%8d%e5%88%97%e3%81%ae%e5%9f%ba%e6%9c%ac%e5%95%8f%e9%a1%8c%e8%a7%a3%e8%aa%ac/
