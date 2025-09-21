#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)

        return heap[0]
# @lc code=end

