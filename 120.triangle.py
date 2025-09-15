#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [n for n in triangle[-1]]

        for r in range(len(triangle) - 2, -1, -1):
            for c in range(r + 1):
                dp[c] = min(dp[c], dp[c + 1]) + triangle[r][c]

        return dp[0]
# @lc code=end

