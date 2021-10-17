from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = []
        result = []

        [nums.append(i) for i in range(0, len(s) + 1)]

        for v in s:
            if v == 'I':
                index = nums.index(min(nums))
                result.append(nums.pop(index))
            elif v == 'D':
                index = nums.index(max(nums))
                result.append(nums.pop(index))

        # 余った最後の要素を結合する
        result.append(nums.pop())
        return result

# 模範解答
# https://leetcode.com/problems/di-string-match/discuss/382097/Solution-in-Python-3-(beats-~100)-(one-line)


'''
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        return (lambda x: [x.pop() if i == 'D' else x.popleft() for i in S]+[x[0]])(collections.deque(range(len(S)+1)))
'''

# https://leetcode.com/problems/di-string-match/discuss/619851/Very-simple-solution-in-python-with-explanations

'''
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        s, l = 0, len(S)
        res = []

        for c in S:
          if c == "I":
              res.append(s)
              s += 1
          else:
              res.append(l)
              l -= 1

        res.append(s)
        return res
'''
