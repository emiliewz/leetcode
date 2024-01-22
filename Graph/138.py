# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        a = {None: None}
        cur = head

        while cur:
            a[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = a[cur]
            copy.next = a[cur.next]
            copy.random = a[cur.random]
            cur = cur.next

        return a[head]
