from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        odd = []

        [result.append(v) for v in nums if v % 2 == 0]
        [odd.append(v) for v in nums if v % 2 == 1]

        result.extend(odd)
        return result
