#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        setSubstring = set()

        def maxUnique(i):
            if i == len(s):
                return 0

            out = 0
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in setSubstring:
                    continue

                setSubstring.add(substr)
                out = max(out, maxUnique(j + 1) + 1)
                setSubstring.remove(substr)

            return out

        return maxUnique(0)
# @lc code=end
