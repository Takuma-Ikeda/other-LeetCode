class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0

        def recur(root, level, isGrandParentEven=False, isParentEven=False):
            def isEven(val):
                return True if (root.val % 2) == 0 else False

            if level == 1:
                isGrandParentEven = isEven(root.val)
            elif level == 2:
                isParentEven = isEven(root.val)
            else:
                if isGrandParentEven:
                    self.result += root.val

                # 世代交代
                isGrandParentEven = isParentEven
                isParentEven = isEven(root.val)

            if root.left:
                recur(root.left, level + 1, isGrandParentEven, isParentEven)

            if root.right:
                recur(root.right, level + 1, isGrandParentEven, isParentEven)

        recur(root, 1)
        return self.result


# 模範解答
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/668270/two-solution-in-python-3-both-bfs-and-dfs


'''
# BFS
def sumEvenGrandparent(self, root: TreeNode) -> int:
	if not root:
		return 0

	q = [root]
	result = 0

	while q:
		curr = q.pop()

		if curr:
			q += [curr.right, curr.left]

			if curr.val % 2 == 0:
				if curr.left:
					if curr.left.left:
						result += curr.left.left.val

					if curr.left.right:
						result += curr.left.right.val

				if curr.right:
					if curr.right.left:
						result += curr.right.left.val

					if curr.right.right:
						result += curr.right.right.val
	return result
'''

'''
# DFS
def sumEvenGrandparent(self, root: TreeNode) -> int:
	stack = [(root, None)]
	result = 0

	while stack:
		node, even_parent = stack.pop()

		if node.left:
			stack.append((node.left, node.val % 2 == 0))

			if even_parent:
				result += node.left.val

		if node.right:
			stack.append((node.right, node.val % 2 == 0))

			if even_parent:
				result += node.right.val

	return result
'''
