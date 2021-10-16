from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(1 for start, end in zip(startTime, endTime) if (start <= queryTime) and (queryTime <= end))

# 模範解答
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/discuss/765800/Python-One-Liner


'''
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([queryTime >= i and queryTime <= j for i, j in zip(startTime, endTime)])
'''
