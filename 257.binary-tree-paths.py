#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtrack(cur, node):
            if not node.left and not node.right:
                out.append("->".join(cur + [str(node.val)]))
                return True

            if node.left:
                backtrack(cur + [str(node.val)], node.left)
            if node.right:
                backtrack(cur + [str(node.val)], node.right)

        out = []
        backtrack([], root)
        return out
# @lc code=end
