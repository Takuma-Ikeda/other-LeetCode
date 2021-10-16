class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

# 模範解答
# https://leetcode.com/problems/goal-parser-interpretation/discuss/961441/Python-one-liner


'''
# 正規表現モジュール re
import re
class Solution:
    def interpret(self, command: str) -> str:
        # 正規表現を使って置換する方が早い
        return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))
'''
