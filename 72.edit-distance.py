#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        height = len(word1) + 1
        width = len(word2) + 1
        table = [[0] * width for _ in range(height)]

        for i in range(height):
            table[i][0] = i
        for j in range(width):
            table[0][j] = j

        for i in range(1, height):
            for j in range(1, width):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j - 1],
                                          table[i][j - 1], table[i - 1][j])

        return table[height - 1][width - 1]
        # @lc code=end
