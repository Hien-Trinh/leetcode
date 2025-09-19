#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()

        for c in s:
            if c != ']':
                stack.append(c)
                continue

            text = ""
            while stack[-1] != '[':
                text = stack.pop() + text

            stack.pop()

            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num

            text *= int(num)
            stack.append(text)

        return "".join(stack)


# @lc code=end

