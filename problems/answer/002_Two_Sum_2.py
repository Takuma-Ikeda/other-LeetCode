from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        head = 1
        tail = len(numbers)

        while head < tail:
            total = numbers[head - 1] + numbers[tail - 1]
            if total < target:
                head += 1
            elif total > target:
                tail -= 1
            else:
                return [head, tail]
