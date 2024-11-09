#
# @lc app=leetcode id=3133 lang=python3
#
# [3133] Minimum Array End
#

# @lc code=start
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i_x = 1
        i_n = 1
        while i_n < n:
            if not i_x & x:
                if i_n & (n - 1):
                    x |= i_x
                i_n <<= 1

            i_x <<= 1

        return x
# @lc code=end
