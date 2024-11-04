#
# @lc app=leetcode id=3163 lang=python3
#
# [3163] String Compression III
#

# @lc code=start
class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return word

        out = ""
        i = 1
        count = 1
        while i < len(word):
            if word[i] == word[i - 1] and count < 9:
                count += 1
            else:
                out += str(count) + word[i - 1]
                count = 1

            i += 1

        return out + str(count) + word[i - 1]

# @lc code=end
