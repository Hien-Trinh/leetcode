#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        goal = n * n

        def coord(pos):
            r, c = divmod(pos - 1, n)
            c = c if r % 2 == 0 else n - c - 1
            r = n - r - 1

            return r, c

        visited = [False] * (n * n + 1)
        visited[1] = True
        queue = deque([(1, 0)])

        while queue:
            cur, steps = queue.popleft()
            for roll in range(1, 7):
                new = cur + roll
                if new > goal:
                    continue
                r, c = coord(new)
                if board[r][c] != -1:
                    new = board[r][c]
                if new == goal:
                    return steps + 1
                if not visited[new]:
                    visited[new] = True
                    queue.append((new, steps + 1))

        return -1
# @lc code=end

