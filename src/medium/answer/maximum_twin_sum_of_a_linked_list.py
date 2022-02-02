from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        max_val = 0

        def recur(head):
            if not head:
                return

            vals.append(head.val)

            if head.next:
                recur(head.next)

        recur(head)

        for v1, v2 in zip(vals, vals[::-1]):
            result = v1 + v2
            max_val = result if result > max_val else max_val

        return max_val


# 模範解答
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/discuss/1680417/C%2B%2B-Python-mid-and-reverse-solution

'''
def pairSum(self, head: Optional[ListNode]) -> int:
    # ランナーテクニック: 最初から巡回するポインタと先の要素から巡回するポインタ 2 つを用意する
	slow, fast = head, head
	maxVal = 0

	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next

	curr, prev = slow, None

	while curr:
		curr.next, prev, curr = prev, curr, curr.next

	while prev:
		maxVal = max(maxVal, head.val + prev.val)
		prev = prev.next
		head = head.next

	return maxVal
'''
