class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def recur(root):
            if not root:
                return

            if root.right:
                recur(root.right)

            self.sum += root.val
            root.val = self.sum

            if root.left:
                recur(root.left)

            return root

        return recur(root)

# 模範解答
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286849/Easy-to-understand-Python-solution-beats-100-reversed-inorder

'''
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def recur(node, sumTillNow):
            if not node:
                return sumTillNow
            node.val += recur(node.right, sumTillNow)
            return recur(node.left, node.val)

        recur(root, 0)
        return root
'''
