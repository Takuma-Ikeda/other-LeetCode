class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        result = True
        v1 = coordinates[0:1]
        v2 = int(coordinates[1:2])

        if ord(v1) % 2 == 0:
            result = False
        else:
            result = True

        if v2 % 2 == 0:
            return result
        else:
            return not result


# 模範解答
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/discuss/1140948/PythonPython3-or-Simple-and-Easy-code-or-self-explanatory


'''
class Solution:
    def squareIsWhite(self, c: str) -> bool:
        if c[0] in 'aceg':
            return int(c[1]) % 2 == 0
        elif c[0] in 'bdfh':
            return int(c[1]) % 2 == 1
        return False
'''
