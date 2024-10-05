#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        def buildPath(equations, values):
            for equation, value in zip(equations, values):
                start, end = equation

                if start in graph:
                    graph[start].append((end, value))
                else:
                    graph[start] = [(end, value)]

                if end in graph:
                    graph[end].append((start, 1 / value))
                else:
                    graph[end] = [(start, 1 / value)]

        def findPath(query):
            start, end = query

            if start not in graph or end not in graph:
                return -1

            queue = deque([(start, 1)])
            visited = set()

            while queue:
                node, cur_value = queue.popleft()
                if node == end:
                    return cur_value

                visited.add(node)
                for neighbor, value in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, cur_value * value))

            return -1

        buildPath(equations, values)
        return [findPath(query) for query in queries]
# @lc code=end
