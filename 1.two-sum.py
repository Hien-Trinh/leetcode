#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            if n in table:
                return [table[n], i]
            else:
                table[target - n] = i

# @lc code=end

