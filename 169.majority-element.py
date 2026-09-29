#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    top_candidate, count = nums[0], 1
    for n in nums[1:]:
      if n == top_candidate:
        count += 1
      else:
        count -= 1
        if count == 0:
          top_candidate = n
          count = 1

    return top_candidate
# @lc code=end

