from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 不正解
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         def recur(root, nums):
#             if nums:
#                 # 一番大きい値で配列を左右分割
#                 max_num = max(nums)
#                 left, right = get_left_and_right(max_num, nums)
#                 nums.pop(nums.index(max_num))
#                 print(nums)

#                 if nums:
#                     # 次に大きい値は左右どちらにあるか
#                     max_num = max(nums)
#                     node = TreeNode(max_num)

#                     if max_num in left:
#                         root.left = node
#                         recur(root.left, left)

#                     if max_num in right:
#                         root.right = node
#                         recur(root.right, right)

#             return root

#         def get_left_and_right(max_num, nums):
#             max_idx = nums.index(max_num)
#             return nums[0:max_idx], nums[max_idx + 1:]

#         max_num = max(nums)
#         root = TreeNode(max_num)

#         return recur(root, nums)

# 模範解答
# https://leetcode.com/problems/maximum-binary-tree/discuss/870093/Use-Stack-(Python-O(n)-timespace)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nodes = []

        for num in nums:
            node = TreeNode(num)

            # nodes 末尾の要素の値より大きい場合
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()

            if nodes:
                nodes[-1].right = node

            nodes.append(node)

        return nodes[0]
