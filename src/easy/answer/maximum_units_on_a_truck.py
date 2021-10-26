from typing import List
from collections import defaultdict


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        result = 0
        d = defaultdict(int)

        # numberOfUnitsPerBox => numberOfBoxes のハッシュマップを作成
        for boxType in boxTypes:
            if boxType[1] in d:
                d[boxType[1]] += boxType[0]
            else:
                d[boxType[1]] = boxType[0]

        while count != truckSize:
            item = max(d.items())
            numberOfUnitsPerBox, numberOfBoxes = item[0], item[1]

            # トラックが満タンになってしまう場合
            if truckSize < (numberOfBoxes + count):
                # 載せられる数
                size = truckSize - count
                result += (size * numberOfUnitsPerBox)
                break
            else:
                # ユニットをすべて詰め込む
                count += numberOfBoxes
                result += (numberOfBoxes * numberOfUnitsPerBox)

            d.pop(numberOfUnitsPerBox)

            # トラックは空いているが boxType が枯渇したパターン
            if not d:
                break

        return result

# 模範解答
# https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999230/Python-Simple-solution


'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = 1)
        s = 0

        for i, j in boxTypes:
            i = min(i, truckSize)
            s += i * j
            truckSize -= i

            if truckSize == 0:
                break

        return s
'''
