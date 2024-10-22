#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []

        def backtrack(cur, turnedOn, start):
            if cur[0] > 11 or cur[1] > 59:
                return
            if turnedOn == 0:
                out.append('%d:%02d' % (cur[0], cur[1]))
                return

            for i in range(start, 10):
                if i < 4:
                    backtrack([cur[0] | 1 << i, cur[1]], turnedOn - 1, i + 1)
                else:
                    j = i - 4
                    backtrack([cur[0], cur[1] | 1 << j], turnedOn - 1, i + 1)

        out = []
        backtrack([0, 0], turnedOn, 0)
        return out
# @lc code=end
