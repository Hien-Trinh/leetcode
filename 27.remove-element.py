#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    for n in nums:
      if n != val:
        nums[i] = n
        i += 1

    return i
# @lc code=end

