#
# @lc app=leetcode id=3097 lang=python3
#
# [3097] Shortest Subarray With OR at Least K II
#

# @lc code=start
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_len = float('inf')
        bits = [0] * 32
        l = 0
        for r in range(len(nums)):
            for i in range(32):
                if nums[r] & (1 << i):
                    bits[i] += 1

            cur = 0
            for i in range(32):
                if bits[i]:
                    cur |= (1 << i)

            while l <= r and cur >= k:
                min_len = min(min_len, r - l + 1)
                for i in range(32):
                    if nums[l] & (1 << i):
                        bits[i] -= 1

                cur = 0
                for i in range(32):
                    if bits[i]:
                        cur |= (1 << i)

                l += 1

        return min_len if min_len != float('inf') else -1
# @lc code=end
