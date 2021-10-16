class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list = s.split(' ')
        while len(list) > k:
            del list[k]
        return ' '.join(list)

# 模範解答
# https://leetcode.com/problems/truncate-sentence/discuss/1142293/2-lines-of-code-with-100-less-space-used


'''
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # splist に区切り文字を入れない場合は ' ' でセパレートする
        return ' '.join(s.split()[:k])
'''
