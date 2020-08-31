class Solution:

    def numberOfSteps (self, num: int) -> int:

        count = 0
        bitstring = bin(num)[2:]
        print(bitstring)

        while num != 0:
            if (num % 2) == 0:
                num = num / 2
            else:
                num = num - 1
            count += 1

        return count

# 模範解答
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/750470/Python%3A-Long-explanation-of-bit-count-method

# 参考) https://suwaru.tokyo/%E3%80%90%E4%B8%80%E8%A6%A7%E8%A1%A8%E3%81%82%E3%82%8A%E3%80%91%E5%8D%81%E9%80%B2%E6%95%B0%E3%81%8B%E3%82%89%E4%BA%8C%E9%80%B2%E6%95%B0%E3%81%B8%E3%81%AE%E5%A4%89%E6%8F%9B%E6%96%B9%E6%B3%95%E3%80%9010/


'''
class Solution:
    def numberOfSteps (self, num: int) -> int:
    
        # 二進法: すべての偶数はビット 0 で終わり、すべての奇数はビット 1 で終わる
        # 最後のビットが 0 のとき 2 で除算する
        # 最後のビットが 1 のとき 1 で減算する
        
        # また十進数の 2 による除算は、二進数の 1 つの右ビットシフトに相当する
        # 例えば 14 / 2 = 7 だが、
        # 14 の二進数である 1110 を「1110 >> 1」すると 111 であり、111 は十進数で 7 である
        
        # つまり、右ビットシフトの回数 が「割り算の回数」であり、
        # 右ビットシフトするたびに、それが奇数だったら減算が必要なので「減算の回数」も数えればよい
        
        # 例えば 16 = 10000 (5ビット) になる
        # 4 ビット右シフト (除算) すると、末尾に 1 ビット (奇数) だけが残る
        # → 1 減算が 1 回必要
        
        # ビット列の長さは「ビットシフトの数 + 1 」で求めることができる、また
        # ビットシフトの数は「ビット列の長さ - 1 」 である。
        # ビットシフトの数は「除算の回数」と同義なので、これをカウントする

        # 例えば 22 = 10110 (5ビット) になる
        # 4 ビット右シフト (除算) すると、末尾に 3 回 1 ビット (奇数) くる
        # → 1 減算が 3 回必要
        # → 減算の回数とは「ビット列の 1 の個数」のことなので、これをカウントする
        
        # したがって答えのステップ数は「(ビット列の長さ - 1 ) + ビット列の 1 の個数」で求めることができる 
        
        # ビット列を取得
        # [2:] でスライスしているのは、頭の '0b' という文字列が不要であるため
        bitstring = bin(num)[2:]        
        count = (len(bitstring) - 1 ) + bitstring.count('1')
        return count
'''
