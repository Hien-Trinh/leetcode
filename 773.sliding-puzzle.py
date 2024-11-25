#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        b = "".join([str(n) for row in board for n in row])
        queue = deque([(b.index("0"), b, 0)])
        visited = set([b])

        while queue:
            zero_idx, cur_board, step = queue.popleft()
            if cur_board == "123450":
                return step

            cur_board = list(cur_board)

            for new_idx in adj[zero_idx]:

                cur_board[new_idx], cur_board[zero_idx] = cur_board[zero_idx], cur_board[new_idx]
                b = "".join(cur_board)

                if b not in visited:
                    visited.add(b)
                    queue.append((new_idx, b, step+1))

                cur_board[new_idx], cur_board[zero_idx] = cur_board[zero_idx], cur_board[new_idx]

        return -1
# @lc code=end
