#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        while queue:
            curGene, steps = queue.popleft()
            for i in range(8):
                for l in "ACGT":
                    nextGene = curGene[:i] + l + curGene[i+1:]
                    if nextGene not in bank:
                        continue
                    if nextGene == endGene:
                        return steps + 1
                    queue.append((nextGene, steps + 1))
                    bank.remove(nextGene)

        return -1
# @lc code=end

