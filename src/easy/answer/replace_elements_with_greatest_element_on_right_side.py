from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_index = len(arr) - 1
        return [-1 if (i == last_index) else max(arr[i + 1:]) for i, _ in enumerate(arr)]


# 模範解答
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/discuss/478465/Python-3-Faster-than-99.7-Memory-less-than-100

'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # -1 は必ず存在するので初期値にしておく
        result = [-1]
        greatest = 0

        for v in arr[::-1]:
            if greatest < v:
                greatest = v

            result.append(greatest)

        result.pop()
        return result[::-1]
'''
