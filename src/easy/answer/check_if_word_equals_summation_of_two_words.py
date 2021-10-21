class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        def convertInt(s) -> int:
            # 先頭 a をトリム
            while s.startswith('a'):
                s = s[1:]

            # 全部 a だった場合
            if not s:
                return 0

            result = []
            [result.append(str(ord(v) - 97)) for v in s]
            return int(''.join(result))

        return (convertInt(firstWord) + convertInt(secondWord)) == convertInt(targetWord)

# 模範解答
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/discuss/1239905/Python-Simple-Solution


'''
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
    numeric_total = lambda s: int(''.join([str(ord(letter) - ord('a')) for letter in s]))

    # lambda 式を呼び出している
    return numeric_total(firstWord) + numeric_total(secondWord) == numeric_total(targetWor)d
'''
