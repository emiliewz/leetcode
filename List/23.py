# 23. Merge k Sorted Lists
import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = cur = ListNode()
        if not lists:
            return None
        minH = []
        for i, j in enumerate(lists):
            if j:
                heapq.heappush(minH, (j.val, i, j))

        while minH:
            v, i, node = heapq.heappop(minH)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(minH, (node.next.val, i, node.next))

        return res.next
