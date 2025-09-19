#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left = 0
        out = 1
        db = {}

        for right in range(len(s)):
            if s[right] not in db or db[s[right]] < left:
                db[s[right]] = right
                out = max(out, right - left + 1)
            else:
                left = db[s[right]] + 1
                db[s[right]] = right

        return out
# @lc code=end

