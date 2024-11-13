#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for n in nums:
            out ^= n

        return out
# @lc code=end
