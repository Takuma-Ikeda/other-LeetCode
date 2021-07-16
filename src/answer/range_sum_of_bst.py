class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = 0
        # result += root.val if (low <= root.val <= high) else 0 にした方が見やすい
        result += root.val if (root.val >= low and root.val <= high) else 0

        if root.left is not None:
            result += self.rangeSumBST(root.left, low, high)
        if root.right is not None:
            result += self.rangeSumBST(root.right, low, high)

        return result

# 模範解答
# https://leetcode.com/problems/range-sum-of-bst/discuss/409173/Clean-and-fast(94)-4-line-Python3-code


'''
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None: return 0
        if root.val > R: return self.rangeSumBST(root.left,L,R)
        if root.val < L: return self.rangeSumBST(root.right,L,R)
        return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)      
'''
