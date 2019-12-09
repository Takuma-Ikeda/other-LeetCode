# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # DFS extend to a list (inorder)
        bstList = list()
        def dfs(root):
            if root:
                dfs(root.left)
                bstList.append(root.val)
                dfs(root.right)
        dfs(root)
        # two pointers
        i,j = 0, len(bstList)-1
        while i < j:
            if bstList[i] + bstList[j] == k:
                return True
            elif bstList[i] + bstList[j] < k:
                i += 1
            else:
                j -= 1
        return False
