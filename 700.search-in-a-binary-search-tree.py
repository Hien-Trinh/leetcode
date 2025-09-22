#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bfs(root, val):
            if val == root.val:
                return root
            elif val < root.val and root.left:
                return bfs(root.left, val)
            elif val > root.val and root.right:
                return bfs(root.right, val)

            return

        if not root:
            return

        return bfs(root, val)
# @lc code=end

