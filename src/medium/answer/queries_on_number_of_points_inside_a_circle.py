from typing import List
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
