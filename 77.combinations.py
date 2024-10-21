#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(cur, start):
            if len(cur) == k:
                out.append(cur)

            for i in range(start, n):
                backtrack(cur + [i + 1], i + 1)

        out = []
        backtrack([], 0)
        return out
# @lc code=end
