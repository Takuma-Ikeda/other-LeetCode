from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # スライスで i + 1 スタートで最後の要素までのリストを作成
            if (target - nums[i]) in nums[i + 1:]:
                # List.index(値) で該当する添字を返却
                # タプルで return
                return [i, nums.index(target - nums[i], i + 1)]


# in 演算子について

'''
https://note.nkmk.me/python-in-basic/
'''

# スライスについて

'''
scores = [40, 50, 70, 90, 60]

# index 1 から 3  (4 未満) の要素でリストを作りたい [50, 70, 90]
print(scores[1:4])

# 一番前から index 1 まで (2 未満) の要素でリストを作りたい [40, 50]
print(scores[:2])

# index 3 から最後の要素までの要素でリストを作りたい [90, 60]
print(scores[3:])

# 一番後ろの index から 3 つ分の要素でリストを作りたい [70, 90, 60]
print(scores[-3:])

# 文字列のスライス

s = "hello"
print(s[1:4]) # ell
'''
