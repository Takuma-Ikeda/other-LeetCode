from typing import List


class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            count = 0
            for target in range(len(nums)):
                if n > nums[target]:
                    count += 1
            result += [count]

        return result

# 模範解答
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/673630/python-3-solution-faster-than-99


'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        # ハッシュマップ
        dic = {}
        
        # 昇順にソートする
        sorted_list = sorted(nums)
        print(sorted_list)
    
        for i, n in enumerate(sorted_list):
            if n not in dic:
                dic[n] = i
        
        # ソート前の順番に合うように結果を作成する
        return [dic[n] for n in nums]
'''
