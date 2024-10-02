#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return True

            nonlocal prev
            if not inorder(node.left) or prev >= node.val:
                return False

            prev = node.val

            return inorder(node.right)

        prev = float('-inf')
        return inorder(root)
# @lc code=end
