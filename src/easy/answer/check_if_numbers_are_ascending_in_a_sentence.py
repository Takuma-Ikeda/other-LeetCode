class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        nums = []
        result = True

        [nums.append(int(w)) for w in words if w.isdigit()]
        # ウォルラス構文
        [result := False for i in range(1, len(nums)) if nums[i] <= nums[i - 1]]

        return result


# 模範解答
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/discuss/1525219/Python3-2-line


'''
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if w.isdigit()]
        # all(): すべての要素が True 判定であること
        # https://note.nkmk.me/python-all-any-usage/
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))
'''
