#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(board, i, j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != "O":
                return

            board[i][j] = "S"

            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)

        for i in range(m):
            if board[i][0] == "O":
                dfs(board, i, 0)
            if board[i][-1] == "O":
                dfs(board, i, n - 1)

        for j in range(n):
            if board[0][j] == "O":
                dfs(board, 0, j)
            if board[-1][j] == "O":
                dfs(board, m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

# @lc code=end
