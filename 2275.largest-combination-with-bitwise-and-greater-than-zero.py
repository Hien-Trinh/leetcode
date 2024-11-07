#
# @lc app=leetcode id=2275 lang=python3
#
# [2275] Largest Combination With Bitwise AND Greater Than Zero
#

# @lc code=start
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(1 << i & n > 0 for n in candidates) for i in range(24))

        # @lc code=end
