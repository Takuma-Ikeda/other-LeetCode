class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/discuss/755030/Super-Short-Python3-Beats-90
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(o, c):
            if not o:
                return None

            if o == target:
                return c

            # None が返ってきた場合、or の右の処理に遷移
            # TreeNode オブジェクトが返ってきたら、そのまま return
            return traverse(o.left, c.left) or traverse(o.right, c.right)

        return traverse(original, cloned)
