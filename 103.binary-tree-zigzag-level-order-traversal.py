#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, depth):
            if node:
                if depth >= len(out):
                    out.append([])
                if depth % 2 == 0:
                    out[depth].append(node.val)
                else:
                    out[depth].insert(0, node.val)

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        out = []
        dfs(root, 0)
        return out
# @lc code=end
