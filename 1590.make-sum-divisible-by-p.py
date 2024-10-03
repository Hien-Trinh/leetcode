#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        if need == 0:
            return 0

        result = len(nums)
        dp = {0: -1}
        cur = 0

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            dp[cur] = i

            if (cur - need) % p in dp:
                result = min(result, i - dp[(cur - need) % p])

        return result if result < len(nums) else -1
# @lc code=end
