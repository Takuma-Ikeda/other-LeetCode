from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict()
        destination = ''

        # key: 出発地点
        # value: 到着地点
        for path in paths:
            d[path[0]] = path[1]

        for _, v in d.items():
            # 到着地点は key として存在しない
            if v not in d:
                destination = v
                break

        return destination


# 模範解答
# https://leetcode.com/problems/destination-city/discuss/619321/Easy-Python-Solution-99.9-time-100-space.


'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pairs = {}
        for i in paths:
            pairs[i[0]] = i[1]

        for src, dest in paths:
            if dest not in pairs:
                return dest
'''
