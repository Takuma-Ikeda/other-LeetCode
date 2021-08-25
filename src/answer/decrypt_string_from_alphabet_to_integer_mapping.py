class Solution:
    def freqAlphabets(self, s: str) -> str:
        s_list = []

        while '#' in s:
            index = s.find('#')

            # 先頭が 10# - 26# の場合
            if index == 2:
                s_list.append(int(s[:index]))
            else:
                # 先頭に 1 - 9 が集まっているのでパースする
                nums = s[:index - 2]

                for c in nums:
                    s_list.append(int(c))

                # 10# - 26# 部分の処理
                s_list.append(int(s[index - 2:index]))

            # 処理した箇所を削除
            s = s[index + 1:]

        # 残りは 1 - 9 しか残っていないので処理する
        for c in s:
            s_list.append(int(c))

        # Unicode コードポイントと合致させるため 96 加算する
        return ''.join([chr(num + 96) for num in s_list])

# 模範解答
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/discuss/470770/Python-3-(two-lines)-(beats-100)-(16-ms)-(With-Explanation)


'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        # 26 から始まって、カウントダウンしていく
        for i in range(26, 0, -1):
            # 該当箇所を見つけて置換する
            s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        return s
'''
