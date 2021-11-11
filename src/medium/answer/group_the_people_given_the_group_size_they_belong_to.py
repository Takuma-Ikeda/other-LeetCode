from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []

        # groupSize 出現回数をカウント
        d1 = defaultdict(int)

        # groupSize をキーに、該当する List の index を格納
        d2 = defaultdict(list)

        for idx, val in enumerate(groupSizes):
            d1[val] += 1
            d2[val].append(idx)

        for groupSize, count in d1.items():
            loop = 0

            while (count // groupSize) != loop:
                loop += 1
                group = []

                while len(group) != groupSize: group.append(d2[groupSize].pop())

                result.append(group)

        return result
