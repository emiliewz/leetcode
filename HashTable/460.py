# 460. LFU Cache
from collections import defaultdict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0

    def append(self, node):
        pre, nxt = self.left, self.left.next
        pre.next = nxt.prev = node
        node.prev, node.next = pre, nxt
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.right.prev
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.a = {}
        self.size = capacity
        self.freq = 0
        self.freq_list = defaultdict(DLinkedList)

    def update(self, node):
        freq = node.count
        self.freq_list[freq].pop(node)

        if self.freq == freq and not self.freq_list[freq].size:
            self.freq += 1

        node.count += 1
        self.freq_list[freq + 1].append(node)

    def get(self, key: int) -> int:
        if key not in self.a:
            return -1
        cur = self.a[key]
        self.update(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key in self.a:
            cur = self.a[key]
            cur.val = value
            self.update(cur)
        else:
            if self.size == 0:
                cur = self.freq_list[self.freq].pop()
                del self.a[cur.key]
                self.size += 1

            self.size -= 1
            self.freq = 1
            self.a[key] = Node(key, value)
            self.freq_list[1].append(self.a[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
