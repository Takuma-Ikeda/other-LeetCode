class Solution:
    def generateTheString(self, n: int) -> str:
        result = []

        if n % 2 == 0:
            for i in range(n):
                if i == n - 1:
                    result.append('b')
                    break
                else:
                    result.append('a')
        else:
            for i in range(n):
                result.append('a')

        return ''.join(result)

# 模範解答
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/discuss/549921/100-100-Super-Easy-Python3!


'''
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return 'a' * n
        else:
            return "a" * (n - 1) + 'b'
'''

'''
class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * (n - 1) + 'b' if n % 2 == 0 else 'a' * n
'''
