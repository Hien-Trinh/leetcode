#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            out += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len(word1):
            out += word1[i:]
        else:
            out += word2[j:]

        return out
# @lc code=end

