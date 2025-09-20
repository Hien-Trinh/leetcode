#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_time = []
        for time in timePoints:
            h = int(time[0:2])
            m = int(time[3:])
            minutes = h * 60 + m
            sorted_time.append(minutes)

        sorted_time.sort()
        out = 1440 + sorted_time[0] - sorted_time[-1]
        for i in range(len(sorted_time) - 1):
            out = min(out, sorted_time[i+1] - sorted_time[i])

        return out
# @lc code=end

