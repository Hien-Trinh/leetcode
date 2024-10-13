#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []

        for i in range(k):
            num = nums[i][0]
            left = min(left, num)
            right = max(right, num)
            heapq.heappush(min_heap, (num, i, 0))

        res = [left, right]

        while True:
            num, lst_idx, num_idx = heapq.heappop(min_heap)
            num_idx += 1
            if num_idx == len(nums[lst_idx]):
                return res

            new_value = nums[lst_idx][num_idx]
            heapq.heappush(min_heap, (new_value, lst_idx, num_idx))
            right = max(right, new_value)
            left = min_heap[0][0]

            if right - left < res[1] - res[0]:
                res = [left, right]
# @lc code=end
