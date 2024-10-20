#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None

        head = out = ListNode()
        heap = []

        for lst_idx in range(len(lists)):
            if not lists[lst_idx]:
                continue
            heapq.heappush(heap, (lists[lst_idx].val, lst_idx))
            lists[lst_idx] = lists[lst_idx].next

        while True:
            if not heap:
                return head.next

            cur_val, lst_idx = heapq.heappop(heap)
            nxt = lists[lst_idx]
            out.next = ListNode(cur_val)
            out = out.next
            if not nxt:
                continue

            lists[lst_idx] = lists[lst_idx].next
            heapq.heappush(heap, (nxt.val, lst_idx))

# @lc code=end
