from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for i in range(left, right + 1):
            s = str(i)

            if '0' not in s:
                self_dividing = True

                for divide in s:
                    if i % int(divide) != 0:
                        self_dividing = False
                        break

                if self_dividing:
                    result.append(i)

        return result

# 模範解答
# https://leetcode.com/problems/self-dividing-numbers/discuss/939511/Python-Beats-98


'''
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for val in range(left, right + 1):
            number = val
            isVal = True

            while number != 0:
                check = number % 10

                if (check == 0) or (val % check != 0):
                    isVal = False
                    break

                # 桁数を減らして次のループへ
                number //= 10

            if isVal:
                res.append(val)

        return res
'''

# https://leetcode.com/problems/self-dividing-numbers/discuss/441078/Accepted-Python-Answer%3A-Easy-to-Understand


'''
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        d = []

        for i in range(left, right + 1):
            # ゾロ目はまとめる
            n = set(str(i))

            if '0' in n:
                continue

            s = True

            for div in n:
                if i % int(div) != 0:
                    s = False
                    break

            if s == True:
                d.append(i)

        return d
'''
