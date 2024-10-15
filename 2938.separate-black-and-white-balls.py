#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#

# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:
        out = 0
        left = 0
        for i in range(len(s)):
            if s[i] == "0":
                out += i - left
                left += 1

        return out
        # @lc code=end
