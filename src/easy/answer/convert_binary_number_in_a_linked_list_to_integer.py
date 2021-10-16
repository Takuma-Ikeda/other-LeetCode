class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 模範解答
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/455239/Python-Simple.-20ms.


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0

        while head:
            binary = head.val
            # 十進数に変換
            # 末尾にバイナリ追加された後の十進数 = (2 * 十進数) + 末尾に追加されるバイナリ
            decimal = (2 * decimal) + binary
            head = head.next

        return decimal


# 模範解答
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/discuss/541833/Python3%3A-simple-16ms-11.9MB-faster-and-smaller-O(n)-complexity


'''
def get_value(self, head, s):
    if head.next is not None:
        # 関数の再起実行
        return self.get_value(head.next, 2 * s + head.val)
    return 2 * s + head.val
'''
