#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad, dire = deque(), deque()
        tail = len(senate)

        for i, party in enumerate(senate):
            if party == 'R':
                rad.append(i)
            else:
                dire.append(i)

        while rad and dire:
            r = rad.popleft()
            d = dire.popleft()

            if r < d:
                rad.append(tail)
            else:
                dire.append(tail)

            tail += 1

        return "Radiant" if rad else "Dire"
# @lc code=end

