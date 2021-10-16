from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = 0
        v1 = edges[0][0]
        v2 = edges[0][1]

        for index, edge in enumerate(edges):
            if index == 0:
                continue
            elif index == 1:
                result = v1 if self.isCenter(edge, v1) else v2
            else:
                break
        return result

    def isCenter(self, edge: List[int], value: int) -> bool:
        if edge[0] == value:
            return True
        elif edge[1] == value:
            return True
        return False

# 模範解答
# https://leetcode.com/problems/find-center-of-star-graph/discuss/1108683/3-Python-Solutions


'''
# 集合型 set で籍集合 & を利用する：共通要素の取得
def findCenter(self, e: List[List[int]]) -> int:
    # {1, 2} & {2, 3} の結果は {2}
    return (set(e[0]) & set(e[1])).pop()
'''

'''
def findCenter(self, e: List[List[int]]) -> int:
    if (e[0][0] == e[1][0]) or (e[0][0] == e[1][1]):
        return e[0][0]
    return e[0][1]
'''
