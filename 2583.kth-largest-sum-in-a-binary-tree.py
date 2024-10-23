#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import deque


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        queue.append(root)
        heap = []

        while queue:
            cur = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                cur += node.val

            heapq.heappush(heap, cur)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0] if len(heap) == k else -1

# @lc code=end
