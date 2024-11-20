#
# @lc app=leetcode id=2516 lang=python3
#
# [2516] Take K of Each Character From Left and Right
#

# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limit = {char: s.count(char) - k for char in 'abc'}
        if any(count < 0 for count in limit.values()):
            return -1

        counter = {char: 0 for char in 'abc'}
        out = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            counter[char] += 1

            while counter[char] > limit[char]:
                counter[s[left]] -= 1
                left += 1

            out = max(out, right - left + 1)

        return len(s) - out

        # @lc code=end
