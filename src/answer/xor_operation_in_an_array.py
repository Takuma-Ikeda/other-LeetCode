class Solution:

    def xorOperation(self, n: int, start: int) -> int:

        '''
        XOR ビット演算とは
        二進数の XOR ビット演算は ^ で表現できる
        ビットがお互いに違ったら 1 (true) / 同じだったら 0 (false) になる

        例 1 :
        十進数 [0, 2, 4, 6, 8] -> 二進数 [0, 10, 100, 110, 1000]
        0 ^ 10 ^ 100 ^ 110 ^ 1000 -> ビットを揃えると 0000 ^ 0010 ^ 0100 ^ 0110 ^ 1000
        0000 ^ 0010 = 0010
        0010 ^ 0100 = 0110
        0110 ^ 0110 = 0000
        0000 ^ 1000 = 1000
        二進数 1000 は 8 である

        例 2 :
        十進数 [3, 5, 7, 9] -> 二進数 [11, 101, 111, 1001]
        11 ^ 101 ^ 111 ^ 1001 -> ビットを揃えると 0011 ^ 0101 ^ 0111 ^ 1001
        0011 ^ 0101 = 0110
        0110 ^ 0111 = 0001
        0001 ^ 1001 = 1000
        二進数 1000 は 8 である
        '''

        nums = []
        # 二進数 0
        answer = 0b0

        for i in range(n):
            nums += [start + 2 * i]

        for i, n in enumerate(nums):
            if i == 0:
                answer = n
            else:
                answer ^= n

        return answer

# 模範解答
# https://leetcode.com/problems/xor-operation-in-an-array/discuss/698327/Python-Simple-Solution


'''
class Solution:

    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res
'''
