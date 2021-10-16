from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 普通の zip だと短い List の長さに合わせてループ回数が決まってしまう
        # zip_longest であれば長いほうに合わせて、足りない要素の値をどうするかも指定できる
        return ''.join(v1 + v2 for v1, v2 in zip_longest(word1, word2, fillvalue=''))

# 模範解答
# https://leetcode.com/problems/merge-strings-alternately/discuss/1075531/Simple-Python-Solution


'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''

        for i in range(min(len(word1),len(word2))):
            res += word1[i] + word2[i]

        # for ... in 構文の外でも変数 i は有効
        return res + word1[i + 1:] + word2[i + 1:]
'''
