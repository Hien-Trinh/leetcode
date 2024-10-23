#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums) - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1

        if k < 0:
            nums.reverse()
            return

        l = len(nums) - 1
        while l > k and nums[l] <= nums[k]:
            l -= 1

        nums[l], nums[k] = nums[k], nums[l]

        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# @lc code=end
