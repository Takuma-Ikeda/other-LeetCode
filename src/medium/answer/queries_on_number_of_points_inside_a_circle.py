from typing import List
from bisect import bisect_left
import math


# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/discuss/1163133/Python-One-liner
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) <= r for x1, y1 in points) for x0, y0, r in queries]


# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/discuss/1167044/Python-3-512-ms-faster-than-100-using-complex-numbers
class Solution2:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # complex 複素数
        points = list(map(complex, *zip(*points)))
        queries = ((complex(x, y), r) for x, y, r in queries)
        return [sum(abs(p - q) <= r for p in points) for q, r in queries]


# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/discuss/1176328/Python-Bruteforce-and-Sort
class Solution3:
    def isInsideCircle(self, x1, y1, x2, y2, rsq):
        return (y2 - y1) ** 2 + (x2 - x1) ** 2 <= rsq

    def bruteforce(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []

        for x1, y1, r in queries:
            rsq = r ** 2
            result.append(sum([self.isInsideCircle(x1, y1, x2, y2, rsq) for x2, y2 in points]))

        return result

    def efficient(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        X_MIN, X_MAX = 0, 500
        points.sort()
        result = []

        for x1, y1, r in queries:
            rsq = r ** 2
            l, r = bisect_left(points, [x1 - r, X_MIN]), bisect_left(points, [x1 + r, X_MAX])
            result.append(sum([self.isInsideCircle(x1, y1, x2, y2, rsq) for x2, y2 in points[l:r]]))

        return result
