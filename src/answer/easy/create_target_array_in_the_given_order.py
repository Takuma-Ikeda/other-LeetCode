from typing import List


class Solution:

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        target = []

        for i in range(len(nums)):
            n = nums[i]
            i = index[i]
            target.insert(i, n)

        return target

# 模範解答
# https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/553334/Python-Using-insert()-and-without-insert()


'''
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            # 末尾の index に要素追加する場合
            if index[i] == len(target) :
                target.append(nums[i])
            else:
                # リストの前半スライス + 要素追加 + リストの後半スライス
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target
'''
