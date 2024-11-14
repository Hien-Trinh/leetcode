#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) >> 1
            if sum((quantity + mid - 1) // mid for quantity in quantities) > n:
                left = mid + 1
            else:
                right = mid

        return left
# @lc code=end
