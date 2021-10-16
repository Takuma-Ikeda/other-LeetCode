class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []

        # 関数内関数であれば vals に値を保存できる
        # 再帰的な間順走査 (Inorder Traversal) で挿入する値を取得
        def inord(node):
            if not node:
                return
            inord(node.left)
            vals.append(node.val)
            inord(node.right)

        inord(root)

        result = TreeNode(vals[0])

        # センチネルを使うことで、ツリーの位置をメモリから失わないようにする (ガベージコレクション対策)
        tmp = result

        for i in vals[1:]:
            tmp.right = TreeNode(i)
            tmp = tmp.right

        return result


'''
# https://leetcode.com/problems/increasing-order-search-tree/discuss/958187/Morris-In-order-traversal-(Python-3-O(n)-time-O(1)-space)
# Morris In-order traversal algorithm
class Solution:
    def increasingBST(self, node: TreeNode) -> TreeNode:
        result = tail = TreeNode()

        while node is not None:
            if node.left is not None:
                now = node.left

                while now.right is not None:
                    now = now.right

                now.right = node
                left, node.left = node.left, None
                node = left
            else:
                tail.right = tail = node
                node = node.right

        return result.right
'''

'''
# 再起で print はできるけど値の保持や return ができなかった
# inord メソッドで定義して、List で結果を持っておけばよかった (それかメンバ変数を定義)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root.left:
            self.increasingBST(root.left)

        print(root.val)

        if root.right:
            self.increasingBST(root.right)
'''
