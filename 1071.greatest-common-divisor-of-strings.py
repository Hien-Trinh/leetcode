#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        i = 0
        i_max = gcd(len(str1), len(str2))
        while i < i_max and str1[i] == str2[i]:
            i += 1

        return str1[:i]
# @lc code=end

