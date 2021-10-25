class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0

        for word in text.split():
            isBroken = False

            for letter in brokenLetters:
                if isBroken:
                    break

                isBroken = letter in word

            result += 0 if isBroken else 1

        return result

# 模範解答
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/discuss/1347412/Python3-two-lines-using-set


'''
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # 各文字の集合型を作成
        brokenLetters = set(brokenLetters)

        # 集合型.intersection() で重複している要素を取得できる
        return sum(len(brokenLetters.intersection(t)) == 0 for t in text.split())
'''
