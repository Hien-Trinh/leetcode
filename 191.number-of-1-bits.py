#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n > 0:
            out += n & 1
            n >>= 1

        return out
# @lc code=end
