#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max, all_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            all_max = max(all_max, curr_max)

        return all_max
# @lc code=end
