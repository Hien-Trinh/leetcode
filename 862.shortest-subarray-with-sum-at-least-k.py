#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        out = float('inf')
        dq = deque([(0, -1)])
        cur = 0

        for i in range(len(nums)):
            cur += nums[i]

            while dq and cur - dq[0][0] >= k:
                out = min(out, i - dq.popleft()[1])

            while dq and dq[-1][0] >= cur:
                dq.pop()

            dq.append((cur, i))

        return out if out != float('inf') else -1
# @lc code=end
