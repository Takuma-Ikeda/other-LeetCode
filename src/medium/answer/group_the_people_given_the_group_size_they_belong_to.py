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

# 模範解答
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/discuss/448447/Python-Simple.-Hashmap.-With-comments-(beats-99)


'''
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        _dict_ = collections.defaultdict(list)

        for idx, i in enumerate(groupSizes):
            _dict_[i].append(idx)

        answer = []

        for key, lst in _dict_.items():
            # key の値だけスキップされるので、適切な開始・終了位置で List をスライス分割できる
            for idx in range(0, len(lst), key):
                answer.append(lst[idx:idx + key])

        return (answer)
'''
