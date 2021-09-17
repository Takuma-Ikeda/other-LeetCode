class Solution:
    def sumBase(self, n: int, k: int) -> int:

        '''
        n = 34, k = 6 の場合

        34 ÷ 6 = 5 余り 4
        5 ÷ 6 = 0 余り 5

        十進数 34 を六進数にすると 54 となる

        (6^1 * 5) + (6^0 * 4) = 34 という感じで十進数に戻すことができる
        '''

        '''
        答えの桁数をまず求めて、List で桁数分の要素をつくって 0 埋めしておく
        '''

        digit = 0

        for i in range(10 ** 9):
            if n < k ** i:
                digit += i
                break

        digits = [0] * digit

        '''
        左の桁の係数から確定させていく
        '''

        index = 0

        for i in range(1, digit + 1):
            # k^x
            j = (k ** (digit - i))

            # k^x の係数を取得
            coefficient = n // j

            digits[index] = coefficient
            index += 1

            # 10 進数に戻して n から減算する
            n -= coefficient * j

        # 桁同士の足し算
        return (sum(i for i in digits))


# 模範解答
# https://leetcode.com/problems/sum-of-digits-in-base-k/discuss/1175067/Python3-self-explained


'''
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0

        # n が 0 になるまで続ける
        while n:
            # divmod(n, k) は (n // k, n % k) のタプルを返す ※ つまり「商・余り」を返す
            # 余り x が「係数」といえる
            n, x = divmod(n, k)

            ans += x

        return ans
'''
