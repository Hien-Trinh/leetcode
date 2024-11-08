#
# @lc app=leetcode id=1829 lang=python3
#
# [1829] Maximum XOR for Each Query
#

# @lc code=start
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cur_xor = 0
        out = []
        mask = (1 << maximumBit) - 1
        for n in nums:
            cur_xor ^= n
            out.append(cur_xor ^ mask)

        return out[::-1]
# @lc code=end
