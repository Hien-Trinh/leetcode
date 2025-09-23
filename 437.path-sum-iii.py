#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, cur_sum):
            if not node:
                return 0
            
            cur_sum += node.val
            if cur_sum - targetSum in prefix:
                count = prefix[cur_sum - targetSum]
            else:
                count = 0

            if cur_sum in prefix:
                prefix[cur_sum] += 1
            else:
                prefix[cur_sum] = 1

            count += dfs(node.left, cur_sum) + dfs(node.right, cur_sum)
            prefix[cur_sum] -= 1

            return count

        return dfs(root, 0)
# @lc code=end

