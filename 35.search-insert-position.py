#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m + 1

        return l if nums[l] >= target else l + 1
# @lc code=end
