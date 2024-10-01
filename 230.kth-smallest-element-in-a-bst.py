#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal out, k

            if not node or out > -1:
                return

            inorder(node.left)
            k -= 1
            if k == 0:
                out = node.val
                return
            inorder(node.right)

        out = -1
        inorder(root)
        return out
# @lc code=end
