from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        if n % 2 != 0:
            for v in range(n):
                if (v == 0) or (v % 2 != 0):
                    result.append(v)
                else:
                    prev = result[v - 1]
                    result.append(prev * -1)
        else:
            for v in range(n):
                if v % 2 != 0:
                    prev = result[v - 1]
                    result.append(prev * -1)
                else:
                    result.append(v + 1)

        return result

# 模範解答
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/discuss/470450/Python3-code%3A-simple-and-readable-with-explanation


'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 != 0:
            ans = [0]
        else:
            ans = []

        # 整数除算
        L = n // 2

        for i in range(1, L + 1):
            ans.append(-i)
            ans.append(i)

        return ans
'''
