#
# @lc app=leetcode id=3254 lang=python3
#
# [3254] Find the Power of K-Size Subarrays I
#

# @lc code=start
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        out = []
        l = 0
        count = 1
        for r in range(len(nums)):
            if r > 0 and nums[r] - nums[r-1] == 1:
                count += 1

            if r - l + 1 > k:
                if nums[l+1] - nums[l] == 1:
                    count -= 1

                l += 1

            if r - l + 1 == k:
                out.append(nums[r] if count == k else -1)

        return out

# @lc code=end
