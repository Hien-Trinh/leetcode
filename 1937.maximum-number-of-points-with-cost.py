#
# @lc app=leetcode id=1937 lang=python3
#
# [1937] Maximum Number of Points with Cost
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        c, r = len(points[0]), len(points)

        for i in range(1, r):
            right = [0] * c
            right[-1] = points[i - 1][-1]
            for j in range(c - 2, -1, -1):
                right[j] = max(points[i - 1][j], right[j + 1] - 1)

            left = points[i - 1][0]
            points[i][0] += max(left, right[0])
            for j in range(1, c):
                left = max(points[i - 1][j], left - 1)
                points[i][j] += max(left, right[j])

        return max(points[-1])
# @lc code=end

