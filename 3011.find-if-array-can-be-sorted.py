#
# @lc app=leetcode id=3011 lang=python3
#
# [3011] Find if Array Can Be Sorted
#

# @lc code=start
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countBits(n):
            return bin(n).count('1')

        cur_bit = countBits(nums[0])
        cur_max, cur_min = nums[0], nums[0]
        prev_max = float('-inf')
        for n in nums:
            new_bit = countBits(n)
            if new_bit == cur_bit:
                cur_max = max(cur_max, n)
                cur_min = min(cur_min, n)
            else:
                if prev_max > cur_min:
                    return False
                cur_bit = new_bit
                prev_max = cur_max
                cur_max, cur_min = n, n

        return cur_min > prev_max

# @lc code=end
