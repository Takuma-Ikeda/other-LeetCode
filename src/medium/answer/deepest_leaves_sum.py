from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        level = 0

        def recur(root, level):
            nonlocal d
            level += 1

            if root.left:
                recur(root.left, level)

            if root.right:
                recur(root.right, level)

            d[level] += root.val

        recur(root, level)
        return d[max(d)]


# 模範解答
# https://leetcode.com/problems/deepest-leaves-sum/discuss/471057/Python-3-(three-lines)-(beats-~99)


'''
class Solution:
    def deepestLeavesSum(self, R: TreeNode) -> int:
        B = [R]

        while B:
            A, B = B, [c for n in B for c in [n.left, n.right] if c != None]
        return sum(a.val for a in A if a.val != None)
'''

# https://leetcode.com/problems/deepest-leaves-sum/discuss/464833/Easy-Python-BFS

'''
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sum = 0
        queue = deque([root])

        while queue:
            sum = 0

            for i in range(len(queue)):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return sum
'''

# https://leetcode.com/problems/deepest-leaves-sum/discuss/1153004/Python-DFS

'''
def deepestLeavesSum(self, root: TreeNode) -> int:
	maxlevel = 0
	tsum = 0

	def dfs(node=root, level=0):
		nonlocal maxlevel, tsum

		if not node:
            return

		dfs(node.left, level + 1)
		dfs(node.right, level + 1)

		if maxlevel < level:
			maxlevel = level
			tsum = 0

		if maxlevel == level:
			tsum += node.val

	dfs()
	return tsum
'''
