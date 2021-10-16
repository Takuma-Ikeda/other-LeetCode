from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)

        for v in range(lowLimit, highLimit + 1):
            count = sum(int(s) for s in str(v))
            d[count] += 1

        return max(d.values())


# 模範解答
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/discuss/1058595/Python3-Solution-or-Well-commented-or-Better-than-94-in-Runtime-and-90-in-Memory-distribution

'''
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def numberSum(number:int)->int:
            sum1 = 0

            while number:
                sum1 += number % 10
                number = number // 10

            return sum1

        hashMap = defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            hash_val = numberSum(i)
            hashMap[hash_val] += 1

        values = hashMap.values()

        return max(values)
'''
