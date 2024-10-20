#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1

        def getBit(length, k):
            if length == 1:
                return "0"

            half = length // 2
            if k <= half:
                return getBit(half, k)
            elif k == half + 1:
                return "1"
            else:
                return "0" if getBit(half, length - k + 1) == "1" else "1"

        return getBit(length, k)
        # @lc code=end
