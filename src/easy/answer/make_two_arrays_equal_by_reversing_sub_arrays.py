from typing import List
from collections import defaultdict


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        result = True
        d = defaultdict(int)

        if len(target) != len(arr):
            return False

        for v in target:
            d[v] += 1

        for v in arr:
            d[v] -= 1

        [result := False for v in d.values() if v != 0]

        return result


# 模範解答
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/discuss/689812/Python-O(n)-by-occurrence-comparison

'''
from collections import Counter

class Solution:
    # Counter(List) すればハッシュマップ構造をいきなり作れる、== で比較もできる
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
'''

'''
class Solution:
    # 加算したカウント数を比較
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_num_occ_dict = {}
        source_num_occ_dict = {}

        for num in target:
            target_num_occ_dict[num] = target_num_occ_dict.get( num, 0 ) + 1

        for num in arr:
            source_num_occ_dict[num] = source_num_occ_dict.get( num, 0 ) + 1

        return target_num_occ_dict == source_num_occ_dict
'''
