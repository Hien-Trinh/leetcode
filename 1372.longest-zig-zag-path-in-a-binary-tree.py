#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def dfs(node, flag, steps):
            if not node:
                return

            self.longest = max(steps, self.longest)

            if flag:
                dfs(node.left, False, steps + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, steps + 1)

        dfs(root, True, 0)
        return self.longest
# @lc code=end

