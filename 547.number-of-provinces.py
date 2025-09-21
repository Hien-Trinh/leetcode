#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        q = deque()
        visited = set()
        n_province = 0

        for city in range(n):
            if city in visited:
                continue

            n_province += 1
            q.append(city)
            while q:
                city = q.popleft()
                if city in visited:
                    continue

                visited.add(city)
                neighbors = isConnected[city]
                for i in range(len(neighbors)):
                    if neighbors[i] == 1:
                        q.append(i)

        return n_province
# @lc code=end

