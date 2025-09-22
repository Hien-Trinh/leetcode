#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            y, x, steps = queue.popleft()
            for dy, dx in directions:
                x_new = x + dx
                y_new = y + dy
                if 0 <= x_new < len(maze[0]) and 0 <= y_new < len(maze) and maze[y_new][x_new] == ".":
                    if x_new == 0 or y_new == 0 or x_new == len(maze[0]) - 1 or y_new == len(maze) - 1:
                        return steps + 1
                    queue.append((y_new, x_new, steps + 1))
                    maze[y_new][x_new] = "+"

        return -1

# @lc code=end

