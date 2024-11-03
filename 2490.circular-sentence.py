#
# @lc app=leetcode id=2490 lang=python3
#
# [2490] Circular Sentence
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        prev = sentence[-1][-1]
        for word in sentence:
            if word[0] != prev:
                return False
            prev = word[-1]

        return True

# @lc code=end
