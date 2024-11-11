#
# @lc app=leetcode id=2601 lang=python3
#
# [2601] Prime Subtraction Operation
#

# @lc code=start
import math


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        sieve = [True] * (max(nums) + 1)
        sieve[1] = False

        for i in range(2, math.ceil(math.sqrt(len(sieve)))):
            if sieve[i]:
                for j in range(i * i, len(sieve), i):
                    sieve[j] = False

        prev = 1
        i = 0
        while i < len(nums):
            diff = nums[i] - prev
            if diff < 0:
                return False

            if sieve[diff] or diff == 0:
                i += 1
                prev += 1
            else:
                prev += 1

        return True

        # @lc code=end
