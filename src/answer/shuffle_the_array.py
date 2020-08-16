from typing import List


class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        l1 = nums[0:n]
        l2 = nums[n:]

        for i in range(len(l1)):
            result.append(l1[i])
            result.append(l2[i])

        return result
