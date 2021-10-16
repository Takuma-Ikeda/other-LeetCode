class Solution:
    def sortSentence(self, s: str) -> str:
        result = ''
        words = s.split()
        d = dict()

        for word in words:
            d[int(word[-1])] = word[:-1]

        for index in range(len(words)):
            # " ".join(d[index + 1]) を使うほうが簡単
            # 最後も return result でよくなる
            result += d[index + 1]
            result += ' '

        return result[:-1]


# 模範解答
# https://leetcode.com/problems/sorting-the-sentence/discuss/1210285/2-Lines-or-Python-Solution-or-Linear-TIme-or-Linear-Memory


'''
class Solution:
    def sortSentence(self, s: str) -> str:
        # index 昇順 並び替え
        word_list = sorted(
            s.split(),                   # List 作成
            key = lambda word: word[-1], # List 要素のを取り回して index 取得
            reverse = False              # 昇順
        )

        # 要素末尾の数字を消して結合
        # join について: https://qiita.com/conf8o/items/d57f74b4bcb67882be37
        return " ".join([word[:-1] for word in word_list])
'''

'''
class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        n = len(word_list)
        
        index_dict = dict()
        for word in word_list:
            index_dict[int(word[-1])] = word[:-1]

        res = ""
        for i in range(1, n+1):
            res += index_dict.get(i, "")
            res += " "

        # rstrip とは right strip の略
        # 文字列を右側かわ読んでいって該当する文字列を削除する。引数を指定しない場合は半角スペース
        return res.rstrip()
'''
