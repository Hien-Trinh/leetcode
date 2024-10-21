#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_set, col_set, box_set = [set() for _ in range(
            9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                row_set[i].add(val)
                col_set[j].add(val)
                box_set[i//3 * 3 + j//3].add(val)

        def backtrack(pos):
            if pos == 81:
                return True

            row, col = divmod(pos, 9)

            if board[row][col] != ".":
                return backtrack(pos + 1)

            box = row//3 * 3 + col//3

            for n in [str(n) for n in range(1, 10)]:
                if n in row_set[row] or n in col_set[col] or n in box_set[box]:
                    continue

                board[row][col] = n
                row_set[row].add(n)
                col_set[col].add(n)
                box_set[box].add(n)

                if backtrack(pos + 1):
                    return True

                board[row][col] = "."
                row_set[row].remove(n)
                col_set[col].remove(n)
                box_set[box].remove(n)

            return False

        backtrack(0)
        return

        # @lc code=end
