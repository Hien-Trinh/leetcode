#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        l = prev
        prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        l.next.next = curr
        l.next = prev

        return dummy.next
# @lc code=end

