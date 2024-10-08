#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True

            visited[course] = - 1
            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            visited[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

# @lc code=end
