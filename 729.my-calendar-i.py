#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class Tree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        node = self
        while True:
            if start >= node.end:
                if not node.right:
                    node.right = Tree(start, end)
                    return True
                node = node.right
            elif end <= node.start:
                if not node.left:
                    node.left = Tree(start, end)
                    return True
                node = node.left
            else:
                return False


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Tree(start, end)
            return True

        return self.root.insert(start, end)

        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)
        # @lc code=end
