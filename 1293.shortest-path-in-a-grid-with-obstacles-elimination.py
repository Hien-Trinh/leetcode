#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0,k,0))
        visited = set()

        while queue:
            x, y, k_left, steps = queue.popleft()
            if (x, y, k_left) in visited or k_left < 0:
                continue
            if x == n - 1 and y == m - 1:
                return steps
            visited.add((x, y, k_left))
            if grid[y][x] == 1:
                k_left -= 1

            steps += 1
            if x - 1 >= 0:
                queue.append((x - 1, y, k_left, steps))
            if x + 1 < n:
                queue.append((x + 1, y, k_left, steps))
            if y - 1 >= 0:
                queue.append((x, y - 1, k_left, steps))
            if y + 1 < m:
                queue.append((x, y + 1, k_left, steps))

        return -1

# @lc code=end

