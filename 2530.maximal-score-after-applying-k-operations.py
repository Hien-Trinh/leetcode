#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0

        for _ in range(k):
            value = -heapq.heappop(nums)
            res += value
            heapq.heappush(nums, -ceil(value / 3))

        return res
# @lc code=end
