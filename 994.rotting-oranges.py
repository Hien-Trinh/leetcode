#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        ans = 0
        count_orange = 0
        count_2 = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 2:
                    queue.append((x, y))
                    count_2 += 1
                    count_orange += 1
                elif grid[y][x] == 1:
                    count_orange += 1

        while queue and count_2 < count_orange:
            ans += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_y][new_x] == 1:
                        count_2 += 1
                        grid[new_y][new_x] = 2
                        queue.append((new_x, new_y))

        return ans if count_2 == count_orange else -1
# @lc code=end

