from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        def recur(node, val):
            if node.next:
                val += node.val

                if node.next.val == 0:
                    nodes.append(ListNode(val))
                    val = 0

                recur(node.next, val)

        recur(head, 0)

        for idx, node in enumerate(nodes):
            if len(nodes) > idx + 1:
                node.next = nodes[idx + 1]

        return nodes[0]


# 模範解答
# https://leetcode.com/problems/merge-nodes-in-between-zeros/discuss/1784818/Simple-Python-Solution-in-O(n)-Time


'''
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        ans = ListNode()
        dummy = ans

        while current is not None and current.next is not None:
            if current.val == 0:
                count = 0
                current = current.next

                while current.val != 0 and current is not None:
                    count += current.val
                    current = current.next

                dummy.next = ListNode(count)
                dummy = dummy.next

        return ans.next
'''
