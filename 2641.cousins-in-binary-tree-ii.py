#
# @lc app=leetcode id=2641 lang=python3
#
# [2641] Cousins in Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])

        while queue:
            level_sum = 0
            cousins = defaultdict(list)
            for i in range(len(queue)):
                node, parent = queue.popleft()
                cousins[parent].append(node)

                level_sum += node.val

                if node.left:
                    queue.append((node.left, i))
                if node.right:
                    queue.append((node.right, i))

            for key, value in cousins.items():
                if not value:
                    continue

                if len(value) == 1:
                    value[0].val = level_sum - value[0].val
                else:
                    value[0].val, value[1].val = level_sum - value[0].val - \
                        value[1].val, level_sum - \
                        value[1].val - value[0].val

        return root
# @lc code=end
