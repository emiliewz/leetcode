# 445. Add Two Numbers II
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverse(root):
            prev, cur = None, root

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        l1, l2 = reverse(l1), reverse(l2)
        k = 0
        res = ListNode()
        cur = res
        while l1 or l2 or k:
            i = l1.val if l1 else 0
            j = l2.val if l2 else 0

            v = i + j + k
            digit = v % 10
            k = v // 10

            cur.next = ListNode(digit)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return reverse(res.next)
