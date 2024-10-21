#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur, start, target):
            if target < 0:
                return

            if target == 0:
                out.append(cur)
                return

            for i in range(start, len(candidates)):
                backtrack(cur + [candidates[i]], i, target - candidates[i])

        out = []
        backtrack([], 0, target)
        return out
# @lc code=end
