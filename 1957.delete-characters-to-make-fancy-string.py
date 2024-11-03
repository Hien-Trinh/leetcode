#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        i = 1
        counter = 0
        out = s[0]
        while i < len(s):
            if s[i] == s[i - 1]:
                counter += 1
            else:
                counter = 0

            if counter < 2:
                out += s[i]

            i += 1

        return out
# @lc code=end
