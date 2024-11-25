#
# @lc app=leetcode id=1975 lang=python3
#
# [1975] Maximum Matrix Sum
#

# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        out = 0
        n_negative = 0
        max_negative = float('inf')

        for row in matrix:
            for n in row:
                out += abs(n)
                max_negative = min(max_negative, abs(n))
                if n < 0:
                    n_negative += 1

        if n_negative & 1:
            out -= 2 * max_negative

        return out


# @lc code=end
