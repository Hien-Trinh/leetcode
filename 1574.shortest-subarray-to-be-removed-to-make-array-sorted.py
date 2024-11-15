#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r and arr[l] <= arr[l + 1]:
            l += 1
        if l == r:
            return 0
        while r > l and arr[r] >= arr[r - 1]:
            r -= 1

        minRemove = min(len(arr) - l - 1, r)

        for i in range(l + 1):
            if arr[i] <= arr[r]:
                minRemove = min(minRemove, r - i - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break

        return minRemove
        # @lc code=end
