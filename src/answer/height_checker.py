from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 if v1 != v2 else 0 for v1, v2 in zip(heights, sorted(heights)))
