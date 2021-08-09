class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ''
        even_char = ''

        for index, value in enumerate(s):
            if index % 2 == 0:
                even_char = value
                result += value
            else:
                # Unicode のコードポイントを進める
                result += chr(ord(even_char) + int(value))

        return result

# 模範解答
# https://leetcode.com/problems/replace-all-digits-with-characters/discuss/1186143/Python-1-Liner-%2B-Simple-Readable


'''
class Solution:
    def replaceDigits(self, s: str) -> str:
        return ''.join(chr(ord(s[i-1]) + int(s[i])) if s[i].isdigit() else s[i] for i in range(len(s)))
'''

'''
class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = []
        for i, char in enumerate(s):
            # isdigit(): 文字列が数字だったら
            if char.isdigit(): char = chr(ord(s[i-1]) + int(char))
            # += だと新しいインスタンスを生成するので、できるだけ append や join を利用すること
            answer.append(char)
        return ''.join(answer)
'''
