#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        prev = nums[0]
        curr = max(nums[:2])

        for i in range(2, n):
            curr, prev = max(curr, prev + nums[i]), curr

        return curr
# @lc code=end

