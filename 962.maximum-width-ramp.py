#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        max_right = [0] * len(nums)
        cur_max = nums[-1]

        for i in range(len(nums) - 1, -1, -1):
            cur_max = max(cur_max, nums[i])
            max_right[i] = cur_max

        l, r = 0, 1

        while r < len(nums):
            if nums[l] > max_right[r]:
                l += 1
                r += 1
            else:
                r += 1

        return r - l - 1
# @lc code=end
