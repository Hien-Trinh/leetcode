#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        out = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            sum_level = 0

            for _ in range(size):
                node = queue.popleft()
                sum_level += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            out.append(sum_level / size)

        return out

        # @lc code=end
