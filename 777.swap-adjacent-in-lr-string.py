#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        s, r = 0, 0
        while s < len(start) or r < len(result):
            while s < len(start) and start[s] == 'X':
                s += 1
            while r < len(result) and result[r] == 'X':
                r += 1
            if (r == len(result) or s == len(start)) and s != r:
                return False
            if s == len(start) and r == len(result):
                return True
            if start[s] != result[r]:
                return False
            if start[s] == 'R' and s > r:
                return False
            elif start[s] == 'L' and s < r:
                return False

            s += 1
            r += 1

        return True
# @lc code=end

