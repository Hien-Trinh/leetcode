#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float('inf')

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(close_sum - target):
                    close_sum = cur_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    return cur_sum

        return close_sum
        # @lc code=end
