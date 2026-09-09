#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
  def totalNQueens(self, n: int) -> int:
    count = 0
    cols = set()
    pos_diag = set()
    neg_diag = set()
    def backtrack(row):
      nonlocal count
      if row == n:
        count += 1
        return

      for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
          continue

        count += 1
        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)

        backtrack(row + 1)

        count -= 1
        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)

    backtrack(0)
    return count
# @lc code=end

