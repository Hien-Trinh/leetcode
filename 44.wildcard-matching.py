#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(p) + 1):
            prev = dp[0]
            dp[0] = dp[0] and p[i - 1] == "*"
            for j in range(1, len(s) + 1):
                cur = dp[j]

                if s[j - 1] == p[i - 1] or p[i - 1] == "?":
                    dp[j] = prev
                elif p[i - 1] == "*":
                    dp[j] = dp[j] or dp[j - 1]
                else:
                    dp[j] = False

                prev = cur

        return dp[-1]
# @lc code=end
