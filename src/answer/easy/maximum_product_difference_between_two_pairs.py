from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # sorted() で昇順・降順のインスタンスを作成
        asc = sorted(nums)
        desc = sorted(nums, reverse=True)
        return (desc[0] * desc[1]) - (asc[0] * asc[1])

# 模範解答
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/discuss/1303870/Python3-Two-Solutions%3A-O(nlogn)-and-O(n)-time


'''
def maxProductDifference(self, nums: List[int]) -> int:
       # sort() で昇順にする
       nums.sort()
       return nums[-1] * nums[-2] - nums[0] * nums[1]
'''


'''
def maxProductDifference(self, nums: List[int]) -> int:
       # 浮動小数点を作成する float 関数
       # inf とは無限大のこと
       # -inf とは負の無限大のこと
       
       # min の初期値には無限大を設定しておき、無限大以下の値がきたら更新するようにする
       min1 = min2 = float('inf')
       # max の初期値には負の無限大を設定しておき、負の無限大以上の値がきたら更新するようにする
       max1 = max2 = float('-inf')

       for n in nums:
           if n <= min1:
               min1, min2, = n, min1
           elif n < min2:
               min2 = n

           if n >= max1:
               max1, max2 = n, max1
           elif n > max2:
               max2 = n

       return max1 * max2 - min1 * min2
'''
