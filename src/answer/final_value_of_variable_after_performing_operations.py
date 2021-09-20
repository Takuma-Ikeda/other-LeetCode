from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for v in operations:
            if '++' in v:
                result += 1
            if '--' in v:
                result -= 1

        return result


# 模範解答
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/discuss/1472568/Python3-A-Simple-Solution-and-A-One-Line-Solution

'''
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '+' in o else -1 for o in operations)
'''
