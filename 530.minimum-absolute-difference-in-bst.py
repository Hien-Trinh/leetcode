#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return

            nonlocal prev, out

            dfs(node.left)
            out = min(out, node.val - prev)
            prev = node.val
            dfs(node.right)

        out = 10**5
        prev = -10**5
        dfs(root)
        return out
