#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        cur_sum = 0
        cur_set = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] not in cur_set:
                cur_sum += nums[right]
                cur_set.add(nums[right])

                if right - left + 1 == k:
                    max_sum = max(max_sum, cur_sum)
                    cur_sum -= nums[left]
                    cur_set.remove(nums[left])
                    left += 1

            else:
                while nums[left] != nums[right]:
                    cur_sum -= nums[left]
                    cur_set.remove(nums[left])
                    left += 1

                left += 1

        return max_sum

        # @lc code=end
