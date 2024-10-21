#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(cur, start, target):
            if target < 0:
                return

            if target == 0:
                out.append(cur)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                n = candidates[i]
                backtrack(cur + [n], i + 1, target - n)

        out = []
        backtrack([], 0, target)
        return out

# @lc code=end
