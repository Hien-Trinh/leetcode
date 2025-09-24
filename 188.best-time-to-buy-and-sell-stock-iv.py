#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        prev = [0] * n
        cur = [0] * n
        for i in range(1, k+1):
            minSell = -prices[0]
            for j in range(1, n):
                cur[j] = max(cur[j-1], minSell + prices[j])
                minSell = max(minSell, prev[j] - prices[j])
            prev = cur
            cur = [0] * n

        return prev[-1]
# @lc code=end

