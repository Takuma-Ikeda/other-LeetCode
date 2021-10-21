from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # None の可能性がある場合は Optional 型を使う
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        result = None

        def search(root, val):
            if root.val == val:
                nonlocal result
                result = root

            if root.left is not None:
                search(root.left, val)

            if root.right is not None:
                search(root.right, val)

        search(root, val)
        return result

# 模範解答
# https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/688364/PYTHON-3-BST-or-Easy-to-Read-and-Understand

'''
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
'''
