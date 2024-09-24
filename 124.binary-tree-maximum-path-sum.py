#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMaxPath(node):
            nonlocal max_path
            if not node:
                return 0

            max_left = max(getMaxPath(node.left), 0)
            max_right = max(getMaxPath(node.right), 0)

            cur_path = node.val + max_left + max_right
            max_path = max(max_path, cur_path)

            return node.val + max(max_left, max_right)

        max_path = root.val
        getMaxPath(root)
        return max_path

        # @lc code=end
