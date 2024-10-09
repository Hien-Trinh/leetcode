#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        res = 0

        for p in s:
            if p == "(":
                open += 1
            else:
                if open == 0:
                    res += 1
                else:
                    open -= 1

        return res + open
# @lc code=end
