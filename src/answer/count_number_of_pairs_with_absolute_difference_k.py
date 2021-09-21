from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0

        for i, v1 in enumerate(nums):
            for v2 in nums[i + 1:]:
                if abs(v1 - v2) == k:
                    result += 1

        return result


# 模範解答
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/1471015/Python-Clean-and-concise.-Dictionary-T.C-O(N)

'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # 辞書型の初期化: int を指定すると初期値が 0 に設定されるので、 seen[num] = 0 をしておく必要がなくなる
        seen = defaultdict(int)
        counter = 0

        for num in nums:
            tmp, tmp2 = num - k, num + k

            if tmp in seen:
                counter += seen[tmp]

            if tmp2 in seen:
                counter += seen[tmp2]

            seen[num] += 1
        return counter
'''

'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0

        for num in nums:
            counter += seen[num-k] + seen[num+k]
            seen[num] += 1

        return counter
'''
