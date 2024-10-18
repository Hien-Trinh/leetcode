#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        max_right = "0"
        max_i = -1
        swap_i = -1
        swap_j = -1

        for i in range(len(num) - 1, -1, -1):
            if num[i] > max_right:
                max_right = num[i]
                max_i = i
            elif num[i] < max_right:
                swap_i = i
                swap_j = max_i

        if swap_i != -1:
            num[swap_i], num[swap_j] = num[swap_j], num[swap_i]

        return int("".join(num))
        # @lc code=end
