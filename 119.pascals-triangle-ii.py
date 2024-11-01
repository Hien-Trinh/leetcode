#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex - 1)
        prev.append(1)

        for i in range(len(prev) - 2, 0, -1):
            prev[i] += prev[i - 1]

        return prev
# @lc code=end
