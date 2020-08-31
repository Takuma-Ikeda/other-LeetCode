class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findTarget(self, root, k) -> bool:
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        return self._findTarget(root, set(), k)

    def _findTarget(self, node, nodes, k) -> bool:
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


'''
https://qiita.com/menon/items/657f67bb2817e25b2222
https://python.ms/binary-search-tree/
'''
