from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s = s[::-1] は不可。ローカル変数に参照渡しするだけで、引数 s の値を直接書き換えるわけではない
        # その場でメモリバイトのポイント編集するには s[:] とする
        s[:] = s[::-1]


# 模範解答
# https://leetcode.com/problems/reverse-string/discuss/669726/Several-python-sol-sharing-w-Visualization


'''
# mirror image
class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)

        for i in range(size // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
'''

'''
# 2 Pointer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
'''

'''
# 再起
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper( left:int, right:int, string: List[str]):
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1, s)

        helper(left = 0, right = len(s) - 1, string = s)
'''
