#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
from collections import deque


class Solution:
    def minLength(self, s: str) -> int:
        if not s:
            return 0

        stack = deque()
        for c in s:
            if not len(stack):
                stack.append(c)
                continue

            if c == "B" and stack[-1] == "A":
                stack.pop()
                continue

            if c == "D" and stack[-1] == "C":
                stack.pop()
                continue

            stack.append(c)

        return len(stack)
# @lc code=end
