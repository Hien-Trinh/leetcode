#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            if not node:
                return 0

            if node.val >= maximum:
                maximum = node.val
                count = 1
            else:
                count = 0

            count += dfs(node.left, maximum) + dfs(node.right, maximum)

            return count
            
        return dfs(root, -float('inf'))
# @lc code=end

