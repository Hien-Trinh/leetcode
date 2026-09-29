#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    if len(nums) < 2:
      return len(nums)
    i = 1
    curr = nums[0]
    for n in nums[1:]:
      if n != curr:
        curr = n
        nums[i] = n
        i += 1

    return i

# @lc code=end

