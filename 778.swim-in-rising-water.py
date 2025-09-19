#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        heapq.heappush(q, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))

        while q:
            t, x, y = heapq.heappop(q)
            if x == n - 1 and y == n - 1:
                return t

            if x > 0 and (x-1, y) not in visited:
                heapq.heappush(q, (max(t, grid[y][x-1]), x-1, y))
                visited.add((x-1, y))
            if x < n-1 and (x+1, y) not in visited:
                heapq.heappush(q, (max(t, grid[y][x+1]), x+1, y))
                visited.add((x+1, y))
            if y > 0 and (x, y-1) not in visited:
                heapq.heappush(q, (max(t, grid[y-1][x]), x, y-1))
                visited.add((x, y-1))
            if y < n-1 and (x, y+1) not in visited:
                heapq.heappush(q, (max(t, grid[y+1][x]), x, y+1))
                visited.add((x, y+1))

# @lc code=end

