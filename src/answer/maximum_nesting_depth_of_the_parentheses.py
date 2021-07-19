class Solution:
    def maxDepth(self, s: str) -> int:
        # result = count = 0 と書ける
        result = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
                # result = max(count, result) と書ける
                result = count if count > result else result
            if c == ')':
                count -= 1

        return result

# 模範解答
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/discuss/889316/Python3-O(N)-time-O(1)-space-Maximum-Nesting-Depth-of-the-Parentheses


'''
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                ans = max(ans, cur) # 大きい方の値を返す
            elif c == ')':
                cur -= 1
        return ans 
'''
