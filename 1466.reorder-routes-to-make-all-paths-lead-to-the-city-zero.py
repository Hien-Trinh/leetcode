#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import deque, defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        visited = [False] * n
        ans = 0
        q = deque()
        q.append(0)
        visited[0] = True

        while q:
            city = q.popleft()
            for target, sign in adj[city]:
                if not visited[target]:
                    q.append(target)
                    visited[target] = True
                    ans += sign

        return ans
# @lc code=end

