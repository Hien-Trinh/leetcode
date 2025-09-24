#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        rain = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                rain += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                rain += max_r - height[r]

        return rain
# @lc code=end

