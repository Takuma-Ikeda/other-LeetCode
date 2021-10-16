from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        count = 0
        result = []

        for i in nums:
            count += i
            result.append(count)

        return result
