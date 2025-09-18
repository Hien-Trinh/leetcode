#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        numPrereq = [0] * numCourses
        queue = deque()
        ans = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            numPrereq[course] += 1

        for course in range(numCourses):
            if numPrereq[course] == 0:
                queue.append(course)

        while queue:
            prereq = queue.popleft()
            ans.append(prereq)
            for course in graph[prereq]:
                numPrereq[course] -= 1
                if numPrereq[course] == 0:
                    queue.append(course)

        return ans if len(ans) == numCourses else []
# @lc code=end
