class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {
            'U': 0,
            'D': 0,
            'R': 0,
            'L': 0,
        }

        for v in moves:
            d[v] += 1

        return (d['U'] - d['D'] == 0) and (d['R'] - d['L'] == 0)

# 模範解答
# https://leetcode.com/problems/robot-return-to-origin/


'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
'''
