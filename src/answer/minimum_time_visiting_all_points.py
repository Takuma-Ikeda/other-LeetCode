from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x = y = second = 0

        for index, point in enumerate(points):
            if index == 0:
                # 初期値
                x = point[0]
                y = point[1]
            else:
                while True:
                    if (x == point[0]) and (y == point[1]):
                        break

                    is_add_x = True if x < point[0] else False
                    is_add_y = True if y < point[1] else False

                    # x と y 両方が揃っていない
                    if (x != point[0]) and (y != point[1]):
                        x = self.calc(x, is_add_x)
                        y = self.calc(y, is_add_y)

                    # x は揃っている
                    elif x == point[0]:
                        y = self.calc(y, is_add_y)

                    # y は揃っている
                    elif y == point[1]:
                        x = self.calc(x, is_add_x)

                    second += 1
        return second

    def calc(self, val: int, is_add: bool) -> int:
        return val + 1 if is_add else val - 1

# 模範解答
# https://leetcode.com/problems/minimum-time-visiting-all-points/discuss/832252/Python-3-greater-81.86-faster


'''
def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    steps = 0
    for i in range(len(points) - 1):
        point = points[i]
        next_point = points[i + 1]
        # 次の絶対値のどちらか大きい方がステップ数になる
        steps += max(
            abs(next_point[0] - point[0]), # 「次の x ポイント - 現在の x ポイント」の絶対値
            abs(next_point[1] - point[1])  # 「次の y ポイント - 現在の y ポイント」の絶対値
        )
    return steps
'''
