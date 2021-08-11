class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        num = end = 0
        start = 1
        result = ''

        for index, value in enumerate(s):
            if value == '(':
                num += 1

            if value == ')':
                num -= 1

            if num == 0:
                end = index
                result += s[start:end]
                start = end + 2

        return result

# 模範解答
# https://leetcode.com/problems/remove-outermost-parentheses/discuss/358358/Shortest-Python-Solution


'''
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt, res = 0, ''

        for c in S:
            if c == ')':
                cnt -= 1

            # 0 じゃないときの文字列を結合するだけ
            if cnt != 0:
                res += c

            if c == '(':
                cnt+= 1

        return res
'''
