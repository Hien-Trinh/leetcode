#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        out = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set([(0, 0)])
        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            out.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                seen.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j + 1))

        return out
# @lc code=end

