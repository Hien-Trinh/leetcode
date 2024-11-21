#
# @lc app=leetcode id=2257 lang=python3
#
# [2257] Count Unguarded Cells in the Grid
#

# @lc code=start
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row, col in walls:
            grid[row][col] = 1
        for row, col in guards:
            grid[row][col] = 1

        for row, col in guards:
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                while 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] != 1:
                    grid[nrow][ncol] = 2
                    nrow, ncol = nrow + drow, ncol + dcol

        return sum(row.count(0) for row in grid)


# @lc code=end
