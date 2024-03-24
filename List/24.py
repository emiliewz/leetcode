# 24. Swap Nodes in Pairs
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, head)
        pre, cur = res, head
        while cur and cur.next:
            # save ptrs
            second = cur.next
            later = cur.next.next

            # swap ptrs
            second.next = cur
            cur.next = later
            pre.next = second

            # update ptrs
            pre = cur
            cur = later
        return res.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, cur.next = self, head
        while cur.next and cur.next.next:
            a = cur.next
            b = a.next
            cur.next, b.next, a.next = b, a, b.next
            cur = a
        return self.next
