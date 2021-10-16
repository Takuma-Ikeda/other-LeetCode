class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

# 模範解答
# https://leetcode.com/problems/to-lower-case/discuss/342980/Python-One-Liner


'''
class Solution:
    def toLowerCase(self, str: str) -> str:
        # chr(): ある Unicode コードポイントの文字を return
        # chr(97) -> 'a' を return

        # ord(): ある文字の Unicode コードポイントを return
        # ord('a') -> 97 を return

        # Unicode
        # https://en.wikipedia.org/wiki/List_of_Unicode_characters
        # コードポイント 65 - 90 は 'A' - 'Z'
        # コードポイント 97 - 122 は 'a' - 'z'
        # 大文字から小文字に変換したいなら、大文字のコードポイント +32 すればよい

        return ''.join([chr(ord(char) + 32) if ord(char) in range(65, 91) else char for char in str ])
'''
