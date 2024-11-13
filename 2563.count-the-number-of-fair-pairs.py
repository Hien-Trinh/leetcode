#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def countLessThanTarget(target):
            res, l, r = 0, 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res += r - l
                    l += 1

            return res

        nums.sort()
        return countLessThanTarget(upper) - countLessThanTarget(lower - 1)
# @lc code=end
