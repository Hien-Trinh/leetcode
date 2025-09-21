#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = deque()
        for room in rooms[0]:
            q.append(room)

        while q:
            if len(visited) == len(rooms):
                return True

            room = q.popleft()
            if room in visited:
                continue
            visited.add(room)
            for keys in rooms[room]:
                q.append(keys)

        return len(visited) == len(rooms)
# @lc code=end

