#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x, n):
            if x == 0:
                return 0
            elif n == 0:
                return 1

            t = recur(x, n // 2)
            t *= t
            if n % 2 == 1:
                t *= x * (n % 2)
            return t

        out = recur(x, abs(n))
        if n >= 0:
            return out
        
        return 1 / out
# @lc code=end

