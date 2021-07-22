class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {}

        # String.ascii_lowercase で 'abcdefghijklmnopqrstuvwxyz' を生成できる
        for a in 'abcdefghijklmnopqrstuvwxyz':
            dict[a] = False

        for s in sentence:
            dict[s] = True

        for key, value in dict.items():
            if not value:
                return False

        return True

# 模範解答
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/discuss/1175554/Pangram-Solution-in-Python-3-(96-fast)


'''
import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 集合型を作成
        checker = set(String.ascii_lowercase)
        
        # in 句で真偽値を取得
        for i in checker:
            if i not in sentence.lower():
                return False
        
        return True
'''
