#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        l, r = 1, 1

        cur = chars[0]
        count = 1
        while r < len(chars):
            while r < len(chars) and chars[r] == cur:
                count += 1
                r += 1
            if count > 1:
                for n in str(count):
                    chars[l] = n
                    l += 1

            if r == len(chars):
                break

            cur = chars[r]
            chars[l] = cur
            count = 1
            l += 1
            r += 1

        return l
# @lc code=end

