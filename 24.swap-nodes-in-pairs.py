#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = head
        node1 = head
        node2 = head.next
        prev = None
        count = 2

        while node2:
            if count == 2:
                count = 0
                node1.next = node2.next
                node2.next = node1
                if prev:
                    prev.next = node2
                else:
                    dummy = node2
                prev = node1
                node1 = node2
                node2 = node1.next
            else:
                count += 1
                prev = node1
                node1 = node2
                node2 = node2.next

        return dummy

        # @lc code=end
