#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        l = 0
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                min_length = min(min_length, r - l + 1)
                cur -= nums[l]
                l += 1

        return min_length if min_length != float('inf') else 0
# @lc code=end
