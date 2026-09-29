#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    l, r = m - 1, n - 1
    for i in range(m + n - 1, -1, -1):
      if l < 0:
        nums1[i] = nums2[r]
        r -= 1
      elif r < 0:
        nums1[i] = nums1[l]
        l -= 1
      elif nums1[l] > nums2[r]:
        nums1[i] = nums1[l]
        l -= 1
      else:
        nums1[i] = nums2[r]
        r -= 1

# @lc code=end

