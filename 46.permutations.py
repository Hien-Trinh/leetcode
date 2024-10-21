#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(copy, cur):
            if not copy:
                out.append(cur)
                return

            for i in range(len(copy)):
                dfs(copy[:i] + copy[i+1:], cur + [copy[i]])

        dfs(nums, [])
        return out
# @lc code=end
