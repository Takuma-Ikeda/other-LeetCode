class Solution:

    def maximum69Number(self, num: int) -> int:
        result = ''
        is_changed = False
        str_num = str(num)

        for digit in range(len(str(num))):
            if (str_num[digit:digit + 1] == '6') and (not is_changed):
                result += '9'
                is_changed = True
            else:
                result += str_num[digit:digit + 1]

        return int(result)

# 模範解答
# https://leetcode.com/problems/maximum-69-number/discuss/486561/Python-beats-100-no-string-conversion


'''
class Solution:

# 文字列変換なし
def maximum69Number (num):
    i = j = 0
    original_num = num

    while num != 0:
        # i はただのカウンター
        i += 1

        # digit 取得
        d = num % 10

        if d == 6:
            # 何桁目が 6 なのか j で保持する
            j = i

        # // は整数除算 (切り捨て除算)
        # 5 // 2 なら 2 になる
        # 1.7 // 0.6 なら 2.0 になる
        # num //= 10 することで桁数がひとつ減るし、最後は num が 0 になって while を抜ける
        num //= 10

    # pow: べき乗計算
    # pow(5, 2) なら 25 を取得する
    # 回答に必要な差分を足し算する (num が 6999 だったら 6666 + 3000 して 9999 を返却する)
    return original_num + int(pow(10, j - 1)) * 3
'''
