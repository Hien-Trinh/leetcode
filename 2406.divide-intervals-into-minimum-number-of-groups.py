#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])

        starts.sort()
        ends.sort()
        min_group = 1
        s = e = 0

        while s < len(starts):
            if starts[s] > ends[e]:
                e += 1
            else:
                s += 1
            min_group = max(min_group, s - e)

        return min_group


# @lc code=end
