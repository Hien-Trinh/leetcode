#
# @lc app=leetcode id=1861 lang=python3
#
# [1861] Rotating the Box
#

# @lc code=start
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for r in range(len(box)):
            i = len(box[0]) - 1
            for c in range(len(box[0]) - 1, -1, -1):
                if box[r][c] == '#':
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == '*':
                    i = c - 1

        out = []
        for c in range(len(box[0])):
            col = []
            for r in range(len(box) - 1, -1, -1):
                col.append(box[r][c])
            out.append(col)

        return out

# @lc code=end
