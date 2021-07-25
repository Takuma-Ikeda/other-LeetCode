from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        length = len(arr)
        for num in range(length + 1):
            if num % 2 == 0:
                continue

            start = 0
            end = num
            while True:
                if end > length:
                    break
                result += sum(arr[start:end])
                start += 1
                end = start + num

        return result

# 模範解答
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/943380/Python-Simple-Solution


'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                s += sum(arr[i:j+1])
        return s
'''
