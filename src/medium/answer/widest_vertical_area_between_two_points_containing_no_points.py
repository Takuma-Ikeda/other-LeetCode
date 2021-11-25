from typing import List

class Solution:
    # ダメだった回答
    '''
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        d = defaultdict(list)

        for idx, point in enumerate(points):
            d[point[0]].append(idx)

        max_y_idx = 0
        max_y_val = 0

        for k, l in d.items():
            # 回答の対象となるのは x 軸には少なくとも 2 つ以上の値がある場合のみ
            if len(l) > 1:
                for idx in l:
                    # y 軸の値を取り出す
                    max_y_val = points[idx][1] if points[idx][1] > max_y_val else max_y_val

                    if points[idx][1] == max_y_val:
                        max_y_idx = idx

        return max_y_idx
    '''

    # 模範解答
    # widest vertical area between two points such that no points are inside the area.
    # 「一番離れた x 軸と、それに一番近い x 軸との差」を返す問題
    # https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/discuss/918765/python3-(5-lines)easy-solution-with-comments
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # x 軸で昇順ソートして、x 軸の値だけが入った list 作成
        arr = sorted(x for x, y in points)
        max_dist = 0

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if max_dist < diff:
                max_dist = diff

        return max_dist
