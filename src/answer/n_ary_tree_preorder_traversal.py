from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def preorder_traveral(root):
            if root is not None:
                result.append(root.val)
                if root.children is not None:
                    for node in root.children:
                        preorder_traveral(node)

        preorder_traveral(root)
        return result


# 模範解答
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/541727/Iterative-and-Recursive-or-Easy-to-Understand-or-Faster-or-Simple-or-Python-Solution

'''
class Solution:
    def iterative(self, root):
            if not root: return []
            stack = [root]
            out = []

            while len(stack):
                temp = stack.pop()
                out.append(temp.val)
                stack.extend(reversed(temp.children))

            return out
'''

'''
class Solution:
    def recursive(self, root):
        def rec(root):
            if root:
                out.append(root.val)
                for i in root.children:
                    rec(i)

        out = []
        rec(root)
        return out
'''
