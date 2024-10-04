#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = 2 * sum(skill) // len(skill)
        chemistry = 0
        count = Counter(skill)

        for val, n in count.items():
            if n != count[target - val]:
                return -1
            chemistry += val * (target - val) * n

        return chemistry // 2

        # @lc code=end
