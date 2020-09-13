from functools import reduce
from operator import mul


class Solution:

    def subtractProductAndSum(self, n: int) -> int:

        l = [int(digit) for digit in list(str(n))]

        # Python3.8 以降の場合
        # product_of_digits = math.prod(l)

        '''
        高階関数 reduce
            第 1 引数: function(必須)
            第 2 引数: iterable(必須)
            第 3 引数: initializer(オプション)
            
        operator.mul (multiply)
            reduce の第 2 引数で渡したリストから要素を取り出して、互いの要素を掛け算させる
        '''

        product_of_digits = reduce(mul, l, 1)
        # sum_of_digits = reduce(add, l, 0)
        sum_of_digits = sum(l)

        return product_of_digits - sum_of_digits
