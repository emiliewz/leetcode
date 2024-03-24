# 61. Rotate List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode()
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
        if not k % size:
            return head
        k = size - k % size
        cur = head
        while k > 1:
            cur = cur.next
            k -= 1
        res.next = cur.next
        cur.next = None
        cur = res.next
        while cur.next:
            cur = cur.next
        cur.next = head
        return res.next
