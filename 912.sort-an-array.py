#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
import random
class Solution:
  def sortArray(self, nums: list[int]) -> list[int]:
    def quicksort(head, tail):
      if head >= tail:
        return

      pivot = nums[random.randint(head, tail)]
      lt, gt, i = head, tail, head

      while i <= gt:
        if nums[i] < pivot:
          nums[lt], nums[i] = nums[i], nums[lt]
          lt += 1
          i += 1
        elif nums[i] > pivot:
          nums[gt], nums[i] = nums[i], nums[gt]
          gt -= 1
        else:
          i += 1

      quicksort(head, lt - 1)
      quicksort(gt + 1, tail)

    quicksort(0, len(nums) - 1)
    return nums
# @lc code=end

