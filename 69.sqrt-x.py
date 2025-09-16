#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 1, x // 2
        while l <= r:
            mid = (l + r) // 2
            n = mid * mid
            if n < x:
                l = mid + 1
            elif n > x:
                r = mid - 1
            else:
                return mid

        return r
# @lc code=end

