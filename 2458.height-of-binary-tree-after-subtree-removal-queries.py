#
# @lc app=leetcode id=2458 lang=python3
#
# [2458] Height of Binary Tree After Subtree Removal Queries
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        Depth = defaultdict()
        Height = defaultdict()
        cousins = defaultdict(list)

        def dfs(node, depth):
            if not node:
                return -1

            Depth[node.val] = depth
            cur = 1 + max(dfs(node.left, depth + 1),
                          dfs(node.right, depth + 1))
            Height[node.val] = cur

            return cur

        dfs(root, 0)

        for val, depth in Depth.items():
            cousins[depth].append((Height[val], val))
            cousins[depth].sort(reverse=True)
            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        ans = []
        for query in queries:
            depth = Depth[query]
            if len(cousins[depth]) == 1:
                ans.append(depth - 1)
            elif cousins[depth][0][1] == query:
                ans.append(cousins[depth][1][0] + depth)
            else:
                ans.append(cousins[depth][0][0] + depth)

        return ans
        # @lc code=end
