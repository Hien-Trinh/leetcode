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
        numPrerequisite = [0] * numCourses
        queue = deque()
        out = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            numPrerequisite[course] += 1

        for course in range(numCourses):
            if numPrerequisite[course] == 0:
                queue.append(course)

        while queue:
            prerequisite = queue.popleft()
            out.append(prerequisite)

            for course in graph[prerequisite]:
                numPrerequisite[course] -= 1
                if numPrerequisite[course] == 0:
                    queue.append(course)

        return out if len(out) == numCourses else []
# @lc code=end
