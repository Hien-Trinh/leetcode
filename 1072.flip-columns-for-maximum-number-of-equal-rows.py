#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#

# @lc code=start
from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = Counter()

        for row in matrix:
            if row[0] == 1:
                row = [n ^ 1 for n in row]

            counter[tuple(row)] += 1

        return max(counter.values())

        # @lc code=end
