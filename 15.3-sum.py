#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()

        n, z, p = [], [], []
        for num in nums:
            if num < 0:
                n.append(num)
            elif num == 0:
                z.append(num)
            else:
                p.append(num)

        N, P = set(n), set(p)

        if z:
            for num in N:
                if -num in P:
                    out.add((-num, 0, num))

        if len(z) >= 3:
            out.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    out.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    out.add(tuple(sorted([p[i], p[j], target])))

        return list(out)
# @lc code=end

