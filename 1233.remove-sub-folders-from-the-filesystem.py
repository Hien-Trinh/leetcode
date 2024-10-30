#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.valid_folder = False

    def add(self, path):
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]

        cur.valid_folder = True

    def search(self, path):
        cur = self
        folders = path.split("/")
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            if cur.valid_folder:
                return True

        return False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for f in folder:
            trie.add(f)

        res = []
        for f in folder:
            if not trie.search(f):
                res.append(f)

        return res

        # @lc code=end
