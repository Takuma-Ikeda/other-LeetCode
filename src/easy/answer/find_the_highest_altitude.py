from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        altitude = 0

        for value in gain:
            altitude += value
            if altitude > highest_altitude:
                highest_altitude = altitude

        return highest_altitude

# 模範解答
# https://leetcode.com/problems/find-the-highest-altitude/discuss/1082737/python3-explained-accumulate-solution


'''
from itertools import accumulate

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # accumulate を使うと最初の要素から順番に足し算していった結果 (累積和) の推移をリストで得ることができる
        # 推移の最大値を max で取り出せば OK

        return max(accumulate(gain, initial = 0))
'''
