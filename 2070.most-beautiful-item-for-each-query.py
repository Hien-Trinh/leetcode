#
# @lc app=leetcode id=2070 lang=python3
#
# [2070] Most Beautiful Item for Each Query
#

# @lc code=start
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(query, query_idx)
                         for query_idx, query in enumerate(queries)])
        cur_max = 0
        out = [0] * len(queries)

        item_idx = 0
        for price, idx in queries:
            while item_idx < len(items) and items[item_idx][0] <= price:
                cur_max = max(cur_max, items[item_idx][1])
                item_idx += 1

            out[idx] = cur_max

        return out
# @lc code=end
