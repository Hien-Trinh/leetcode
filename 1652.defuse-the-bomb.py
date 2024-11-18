#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        out = [0] * len(code)
        if k == 0:
            return out

        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]

        cur = sum(code[:k])
        out[-1] = cur
        for l in range(len(code) - 1):
            cur += code[(l + k) % len(code)] - code[l]
            out[l] = cur

        return out
# @lc code=end
