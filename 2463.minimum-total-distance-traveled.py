#
# @lc app=leetcode id=2463 lang=python3
#
# [2463] Minimum Total Distance Traveled
#

# @lc code=start
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        m, n = len(robot), len(factory)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][-1] = float('inf')

        for j in range(n - 1, -1, -1):
            right_most = m - 1

            for i in range(m - 1, -1, -1):
                dist = abs(robot[i] - factory[j][0])

                if dist + dp[i + 1][j] >= dp[i][j + 1]:
                    dp[i][j] = dp[i][j + 1]
                    right_most -= 1
                elif factory[j][1] < right_most - i + 1:
                    dp[i][j] = dist + dp[i + 1][j] - \
                        abs(robot[right_most] - factory[j][0]) - \
                        dp[right_most + 1][j + 1] + dp[right_most][j + 1]
                    right_most -= 1
                else:
                    dp[i][j] = dist + dp[i + 1][j]

        return dp[0][0]

        # @lc code=end
