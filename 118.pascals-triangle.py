#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        triangle = self.generate(numRows - 1)
        prev = triangle[-1]
        cur = [1]

        for i in range(1, len(prev)):
            cur.append(prev[i - 1] + prev[i])

        triangle.append(cur + [1])
        return triangle
# @lc code=end
