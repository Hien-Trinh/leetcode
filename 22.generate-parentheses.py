#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(open, close, current):
            if len(current) == n * 2:
                out.append(current)
                return

            if open < n:
                dfs(open + 1, close, current + '(')

            if open > close:
                dfs(open, close + 1, current + ')')

        out = []
        dfs(0, 0, '')
        return out
# @lc code=end
