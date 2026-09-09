#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    def find_bound(is_left):
      left, right = 0, len(nums) - 1
      bound = -1

      while left <= right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
          bound = mid
          if is_left:
            right = mid - 1
          else:
            left = mid + 1

        elif target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1

      return bound

    return [find_bound(True), find_bound(False)]
# @lc code=end

