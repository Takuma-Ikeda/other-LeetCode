from typing import List


class Solution:

    def decompressRLElist(self, nums: List[int]) -> List[int]:

        result = []

        # 偶数番目
        freq = nums[0::2]
        # 奇数番目
        val = nums[1::2]

        for i in range(len(freq)):
            while 0 != freq[i]:
                result += [val[i]]
                freq[i] -= 1

        return result

# 模範解答
# https://leetcode.com/problems/decompress-run-length-encoded-list/discuss/478426/Python-3-(one-line)-(beats-100)


'''
class Solution:

    def decompressRLElist(self, nums: List[int]) -> List[int]:
    
        l, result = len(nums), []
        
        # range ※ 引数 3 つバージョン
        # 第一引数: start
        # 題ニ引数: stop
        # 第三引数: step (オプション) 数字を刻み方を指定できる
        
        for i in range(0, l, 2):
            # 繰り返し回数 * [値]
            result.extend(nums[i] * [nums[i + 1]])
            
        return result
'''
