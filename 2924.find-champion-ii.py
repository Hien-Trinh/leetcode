#
# @lc app=leetcode id=2924 lang=python3
#
# [2924] Find Champion II
#

# @lc code=start
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        counter = [0] * n

        for _, end in edges:
            counter[end] += 1

        if counter.count(0) == 1:
            return counter.index(0)

        return -1

        # @lc code=end
