from typing import List


class Solution:
    # 解けなかった
    # def minOperations(self, nums: List[int]) -> int:
    #     count = 0

    #     if len(nums) == 1:
    #         return count

    #     for i in range(len(nums) - 1, -1, -1):
    #         if i == 0:
    #             break

    #         if nums[i] <= nums[i - 1]:
    #             nums[i] += 1
    #             count += 1
    #             break

    #     for i, v in enumerate(nums):

    #         if len(nums) -1 == i:
    #             break

    #         next_v = nums[i+1]

    #         while next_v <= v:
    #             next_v += 1
    #             count += 1

    #         nums[i+1] = next_v

    #     return count

    # 模範解答
    # https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/discuss/1178397/Python3-simple-solution-beats-90-users
    def minOperations(self, nums: List[int]) -> int:
        count = 0

        for i in range(1, len(nums)):
            # 一つ前の数字より小さいとしたら
            if nums[i] <= nums[i - 1]:
                x = nums[i]
                nums[i] += (nums[i - 1] - nums[i]) + 1
                count += nums[i] - x

        return count
