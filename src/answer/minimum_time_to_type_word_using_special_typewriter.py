class Solution:
    def minTimeToType(self, word: str) -> int:
        code_points = [97]
        second = 0

        code_points.extend([ord(w) for w in word])

        for i in range(len(code_points)):
            if i == 0:
                continue

            # 時計回り、反時計周りどっちが早いか判定する
            sec1 = abs(code_points[i - 1] - code_points[i])
            sec2 = abs(sec1 - 26)

            # ポインタ移動時間
            second += sec1 if sec1 <= sec2 else sec2

            # タイプ時間
            second += 1

        return second


# 模範解答
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/discuss/1417585/Python3-greedy

'''
class Solution:
    def minTimeToType(self, word: str) -> int:
        # タイプ時間
        ans = len(word)
        prev = "a"

        for ch in word:
            val = (ord(ch) - ord(prev)) % 26
            ans += min(val, 26 - val)
            prev = ch

        return ans
'''
