#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if node:
                if depth == len(out):
                    out.append(node.val)

                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)

        out = []
        dfs(root, 0)
        return out

# @lc code=end
