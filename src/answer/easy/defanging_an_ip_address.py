class Solution:

    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

# 模範解答
# https://leetcode.com/problems/defanging-an-ip-address/discuss/340369/Python-One-Line


'''
# replace() を使うより、こっちの方が早い
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # address を . でパースして [.] で再結合する
        return '[.]'.join(address.split('.'))
'''
