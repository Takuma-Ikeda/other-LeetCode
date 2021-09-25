from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def postoreder_traversal(root):
            if root is not None:
                if isinstance(root, list):
                    for n in root:
                        postoreder_traversal(n.children)
                        result.append(n.val)
                # 初回
                else:
                    postoreder_traversal(root.children)
                    result.append(root.val)

        postoreder_traversal(root)
        return result

# 模範解答
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/541738/Both-iterative-and-recursive-or-Faster-than-95-or-Easy-to-Understand-or-Simple-or-Python


'''
class Solution:
    def postorder(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while len(stack):
            top = stack.pop()
            result.append(top.val)
            # 次の List 要素を取り出して、親の List 要素として結合する: List の長さはひとつ短くなる
            stack.extend(top.children or [])

        # 逆順にするスライス
        return result[::-1]
'''

'''
class Solution:
def postorder(self, root):
    def rec(root):
        if root:
            for c in root.children:
                rec(c)
            result.append(root.val)

    result = []
    rec(root)
    return result
'''
