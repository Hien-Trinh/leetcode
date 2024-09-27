#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.non_overlap = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if start < e and end > s:
                return False

        for s, e in self.non_overlap:
            if start < e and end > s:
                self.overlap.append([max(start, s), min(end, e)])

        self.non_overlap.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end
