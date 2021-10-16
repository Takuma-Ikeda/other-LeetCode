from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []

        for index, i in enumerate(prices):
            is_append = False

            for j in prices[index + 1:]:
                if j <= i:
                    result.append(i - j)
                    is_append = True
                    break

            if not is_append:
                result.append(i)

        return result


# 模範解答
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/discuss/685417/Python-Monotonous-Increasing-Stack-O(N)-solution-100-100

'''
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # prices の index を管理するスタック
        stack = []

        for i, num in enumerate(prices):
            // もっとも最近追加された index を使いたいので [-1] になっている
            while(stack and prices[stack[-1]] >= num):
                popIndex = stack.pop()
                prices[popIndex] -= num

            stack.append(i)

        return prices
'''
