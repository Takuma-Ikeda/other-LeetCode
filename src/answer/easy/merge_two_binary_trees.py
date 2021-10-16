class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        # root1 を root2 に対してマージする
        if (root1 is not None) or (root2 is not None):
            root2.val = root1.val + root2.val

            if (root1.left is not None) and (root2.left is None):
                root2.left = TreeNode()

            if (root1.left is None) and (root2.left is not None):
                root1.left = TreeNode()

            # 再帰
            self.mergeTrees(root1.left, root2.left)

            if (root1.right is not None) and (root2.right is None):
                root2.right = TreeNode()

            if (root1.right is None) and (root2.right is not None):
                root1.right = TreeNode()

            # 再起
            self.mergeTrees(root1.right, root2.right)

        return root2

# 模範解答
# https://leetcode.com/problems/merge-two-binary-trees/discuss/426243/PythonRecursive-Solution-Beats-100


'''
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 存在している方のノードを返す
        if not t1:
            return t2
        elif not t2:
            return t1
        # どっちも存在している場合
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)

        return res
'''
