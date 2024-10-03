#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dp = {0: 1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dp:
                count += dp[sum - k]

            if sum in dp:
                dp[sum] += 1
            else:
                dp[sum] = 1

        return count
# @lc code=end
