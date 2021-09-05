from typing import List
from itertools import combinations


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        XOR の計算について
        2   -> 010
        5   -> 101
        6   -> 110
        XOR -> 001 -> 1
        '''

        '''
        subset (部分集合について)
        s = {'A', 'B', 'C'}

        # True
        {'A', 'B'}.issubset(s)
        # True
        {'A', 'B', 'C'}.issubset(s)
        # False
        {'A', 'D'}.issubset(s)
        '''

        # すべての組み合わせを作成
        combination = []
        for n in range(1, len(nums) + 1):
            # combinations: 組み合わせをタプルで返却
            # 返却するタプルの length は第 2 引数で指定する (つまり 1 〜 最大の組み合わせ桁数を渡す)
            for t in combinations(nums, n):
                # タプルをリストに型変換してから append
                combination.append(list(t))

        answer = 0
        for c in combination:
            xor = 0
            for v in c:
                xor ^= v
            answer += xor

        return answer

# 模範解答
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1211232/Python3-power-set


'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer = 0

        for mask in range(1 << len(nums)):
            val = 0
            for i in range(len(nums)):
                if mask & 1 << i:
                    val ^= nums[i]
            answer += val
        return answer
'''

'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer = 0
        for x in nums:
            answer |= x
        return answer * 2 ** (len(nums) - 1)
'''

# https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1214497/Python-3-5-line-Simple-100-Faster-Combination-%2B-Accumulate

'''
from itertools import combinations, accumulate

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
    answer = 0

    for i in range(1, len(nums) + 1):
        for arr in combinations(nums, i):
            answer += list(accumulate(arr, func=lambda x, y: x ^ y))[-1]

    return answer
'''
