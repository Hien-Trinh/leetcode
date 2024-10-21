#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        counter = Counter(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                out.append(cur)
                return

            for n in counter:
                if counter[n] == 0:
                    continue

                counter[n] -= 1
                dfs(cur + [n])
                counter[n] += 1

        dfs([])
        return out
# @lc code=end
