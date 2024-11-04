#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        isPositive = (dividend > 0) == (divisor > 0)
        out = 0
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend - divisor >= 0:
            x = 0
            while dividend - (divisor << x) >= 0:
                x += 1
            x -= 1
            out += 1 << x
            dividend -= divisor << x

        return out if isPositive else -out
# @lc code=end
