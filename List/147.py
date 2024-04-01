# 147. Insertion Sort List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res.next = cur = head
        while cur and cur.next:
            if cur.val > cur.next.val:
                nodeToInsert = cur.next
                pre = res
                while pre.next.val < nodeToInsert.val:
                    pre = pre.next
                cur.next = cur.next.next

                nodeToInsert.next = pre.next
                pre.next = nodeToInsert
            else:
                cur = cur.next
        return res.next
