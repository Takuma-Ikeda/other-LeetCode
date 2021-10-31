class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/836834/Python-easy-to-understand-DFS
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.total = 0

        def helper(root, nums):
            if not root.left and not root.right:
                nums += str(root.val)
                self.total += int(nums, 2)

            nums += str(root.val)

            if root.left:
                helper(root.left, nums)

            if root.right:
                helper(root.right, nums)

        helper(root, "")
        return self.total

    # https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/836946/Very-easy-DFS-python-solution
    def sumRootToLeaf2(self, root: TreeNode) -> int:
        total = 0

        stack = [(root, str(root.val))]

        while stack:
            node, binVal = stack.pop()

            if node.left:
                stack.append((node.left, binVal + str(node.left.val)))

            if node.right:
                stack.append((node.right, binVal + str(node.right.val)))

            if not node.left and not node.right:
                total += int(binVal, 2)

        return total

    # https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/411429/Python-iterative-DFS-(98.19)
    def sumRootToLeaf3(self, root: TreeNode) -> int:
        # 深さ優先探索 (Depth-First Search: DFS)
        ans = 0
        stack = [(root, 0)]

        while stack:
            node, x = stack.pop()
            x = (2 * x) + node.val

            if not node.left and not node.right:
                ans += x
            else:
                if node.left:
                    stack.append((node.left, x))
                if node.right:
                    stack.append((node.right, x))

        return ans

    def sumRootToLeaf4(self, root: TreeNode) -> int:
        # 前順走査 (Pre-Order Traversal)
        def fn(node):
            nonlocal ans

            if not node:
                return

            stack.append(node.val)

            if node.left is node.right is None:
                ans += int("".join(map(str, stack)), 2)

            fn(node.left) or fn(node.right)
            stack.pop()

        ans, stack = 0, []
        fn(root)

        return ans

    def sumRootToLeaf5(self, root: TreeNode) -> int:
        # 後順走査 (Post-Order Traversal)
        def fn(node, x=0):
            if not node:
                return 0

            x = (2 * x) + node.val

            if node.left is node.right:
                return x

            return fn(node.left, x) + fn(node.right, x)

        return fn(root)
