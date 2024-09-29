#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        table = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                cur = table[j]
                if text1[i - 1] == text2[j - 1]:
                    table[j] = 1 + prev
                else:
                    table[j] = max(cur, table[j - 1])

                prev = cur

        return table[-1]
# @lc code=end
