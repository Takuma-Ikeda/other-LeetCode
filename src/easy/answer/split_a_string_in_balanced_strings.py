class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = count = 0
        for char in s:
            if char == 'L':
                count += 1
            elif char == 'R':
                count -= 1

            if count == 0:
                result += 1
        return result

# 模範解答
# https://leetcode.com/problems/split-a-string-in-balanced-strings/discuss/403688/Python-3-(three-lines)-(beats-100.00-)


'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result, count, dic = 0, 0, {'L':1, 'R':-1}
        for char in s:
            count, result = count + dic[char], result + (count == 0)
        return result
'''
