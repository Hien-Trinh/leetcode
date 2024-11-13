#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        out = [0]
        for i in range(n):
            out += [num | (1 << i) for num in reversed(out)]
        return out
# @lc code=end
