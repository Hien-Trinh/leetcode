#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    if len(nums) < 3:
      return len(nums)
    i = 2
    prev, curr = nums[0], nums[1]
    for n in nums[2:]:
      if curr != n or curr != prev:
        nums[i] = n
        prev = curr
        curr = n
        i += 1

    return i
# @lc code=end

