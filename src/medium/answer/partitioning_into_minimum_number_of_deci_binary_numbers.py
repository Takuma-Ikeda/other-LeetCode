class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0

        [result := int(v) for v in n if int(v) > result]

        return result

# 模範解答
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/discuss/1039096/Detailed-Easiest-Explanation-of-Solution


'''
class Solution:
    def minPartitions(self, n: str) -> int:
        # 文字列はイテレートされるので、桁ごとに取り出されて最大値を判定する
        return max(n)
'''
