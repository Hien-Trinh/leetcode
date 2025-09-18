#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    if word[i] == c:
                        continue

                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordList:
                        queue.append((new_word, step + 1))
                        wordList.remove(new_word)

        return 0
# @lc code=end

