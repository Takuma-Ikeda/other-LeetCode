class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        str1 = word[0:word.find(ch) + 1]
        str2 = word[word.find(ch) + 1:]

        # 反転する
        str1 = str1[::-1]

        return str1 + str2

# 模範解答
# https://leetcode.com/problems/reverse-prefix-of-word/discuss/1459093/Python-3-One-liner-oror-Faster-than-100-(Explained!)


'''
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[:word.index(ch) + 1][::-1] + word[word.index(ch) + 1:] if ch in word else word
'''

'''
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:]
'''
