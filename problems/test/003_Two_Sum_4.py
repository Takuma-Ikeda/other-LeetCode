class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        return self._findTarget(root, set(), k)

    def _findTarget(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val

        # 今まで保存した val の中に答えがあるか調べる
        if complement in nodes:
            return True

        # 現在の val を保存する
        nodes.add(node.val)

        # 左右の node で再帰実行
        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)


n2 = TreeNode(2, None, None)
n4 = TreeNode(4, None, None)
n7 = TreeNode(7, None, None)
n3 = TreeNode(3, n2, n4)
n6 = TreeNode(6, None, n7)
n5 = TreeNode(5, n3, n6)

s = Solution()

print(s.findTarget(n5, 9))
print(s.findTarget(n5, 28))

# BST: Binary Search Tree (二分探索木)

'''
https://qiita.com/menon/items/657f67bb2817e25b2222
https://python.ms/binary-search-tree/
'''
