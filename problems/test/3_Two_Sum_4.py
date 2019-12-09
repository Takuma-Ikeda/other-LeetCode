class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root: TreeNode, k: int) -> bool:
        bstList = list()

        # depth-first search: 深さ優先探索
        def dfs(root):
            if root:
                dfs(root.left)
                bstList.append(root.val)
                dfs(root.right)

        dfs(root)

        i, j = 0, len(bstList) - 1

        while i < j:
            if bstList[i] + bstList[j] == k:
                return True
            elif bstList[i] + bstList[j] < k:
                i += 1
            else:
                j -= 1
        return False


t = TreeNode([5, 3, 6, 2, 4, None, 7])
s = Solution()
print(s.findTarget(t, 9))

# BST: Binary Search Tree (二分探索木)

'''
https://qiita.com/menon/items/657f67bb2817e25b2222
https://python.ms/binary-search-tree/
'''
