# 24. Swap Nodes in Pairs
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, cur.next = self, head
        while cur.next and cur.next.next:
            a = cur.next
            b = a.next
            cur.next, b.next, a.next = b, a, b.next
            cur = a
        return self.next
