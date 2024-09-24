#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(n, t, l):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[t][l] != grid[t + i][l + j]:
                        allSame = False
                        break

            if allSame:
                return Node(grid[t][l], True)

            n = n // 2
            topLeft = build(n, t, l)
            topRight = build(n, t, l + n)
            bottomLeft = build(n, t + n, l)
            bottomRight = build(n, t + n, l + n)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(len(grid), 0, 0)
# @lc code=end
