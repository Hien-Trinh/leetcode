#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return 0

    if nums[0] > nums[1]:
      return 0
    elif nums[-1] > nums[-2]:
      return len(nums) - 1

    left, right = 1, len(nums) - 2
    while left <= right:
      mid = left + (right - left) // 2
      if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
        return mid
      elif nums[mid] < nums[mid + 1]:
        left = mid + 1
      else:
        right = mid - 1

    return -1
# @lc code=end

