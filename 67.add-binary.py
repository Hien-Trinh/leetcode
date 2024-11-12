#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ""
        a_idx, b_idx, carry = len(a) - 1, len(b) - 1, 0

        while a_idx >= 0 or b_idx >= 0:
            if a_idx >= 0:
                carry += ord(a[a_idx]) - ord('0')
            if b_idx >= 0:
                carry += ord(b[b_idx]) - ord('0')

            out += str(carry & 1)
            carry >>= 1
            a_idx -= 1
            b_idx -= 1

        if carry:
            out += str(carry)

        return out[::-1]

# @lc code=end
