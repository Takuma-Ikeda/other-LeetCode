from typing import List


class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        # 子供のキャンディ最大値
        greatest = max(candies)

        for c in candies:
            total = c + extraCandies
            if total >= greatest:
                result += [True]
            else:
                result += [False]

        return result


# 模範解答
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/discuss/609954/Two-python-O(n)-sol.-w-Comment

'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result, maximum = [], max(candies)
        
        for candy in candies:
            if (candy + extraCandies) >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
'''

'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        
        # リスト型の内包表記
        return [(candy + extraCandies) >= maximum for candy in candies]
'''