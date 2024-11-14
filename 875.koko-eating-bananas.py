#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) >> 1
            if sum((pile - 1) // mid + 1 for pile in piles) > h:
                left = mid + 1
            else:
                right = mid

        return left
# @lc code=end
