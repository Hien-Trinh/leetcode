#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [nums[0]]
        for i in range(1, n):
            if not sub or sub[-1] < nums[i]:
                sub.append(nums[i])
            else:
                sub[bisect.bisect_left(sub, nums[i])] = nums[i]

        return len(sub)
# @lc code=end

