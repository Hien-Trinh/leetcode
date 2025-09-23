#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n < 3:
            return tri[n]

        for _ in range(n - 2):
            tri = [tri[1], tri[2], sum(tri)]

        return tri[2]
# @lc code=end

