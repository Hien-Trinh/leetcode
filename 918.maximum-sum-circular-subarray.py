#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, all_max = nums[0], nums[0]
        curr_min, all_min = nums[0], nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            all_max = max(all_max, curr_max)

            curr_min = min(curr_min + nums[i], nums[i])
            all_min = min(all_min, curr_min)

            total += nums[i]

        circular_max = total - all_min
        if circular_max == 0:
            return all_max

        return max(circular_max, all_max)
# @lc code=end

