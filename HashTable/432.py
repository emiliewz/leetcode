# 432. All O`one Data Structure
class Node:
    def __init__(self, s, k):
        self.val = (s, k)
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.left, self.right = Node("", float("inf")), Node("", 0)
        self.left.next, self.right.prev = self.right, self.left
        self.a = {}

    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def insert(self, node):
        pre = self.right.prev
        pre.next = self.right.prev = node
        node.prev, node.next = pre, self.right

    def swap(self, cur, node):
        pre, nxt = cur.prev, node.next
        pre.next, nxt.prev = node, cur
        node.prev, node.next = pre, cur
        cur.prev, cur.next = node, nxt

    def inc(self, key: str) -> None:
        if key in self.a:
            cur = self.a[key]
            cur.val = (key, cur.val[1] + 1)
            while cur.prev and cur.prev.val[1] < cur.val[1]:
                self.swap(cur.prev, cur)
        else:
            self.a[key] = Node(key, 1)
            self.insert(self.a[key])

    def dec(self, key: str) -> None:
        cur = self.a[key]
        cur.val = (key, cur.val[1] - 1)
        if cur.val[1] == 0:
            self.a.pop(key)
            self.remove(cur)
        else:
            while cur.next.val[1] > cur.val[1]:
                self.swap(cur, cur.next)

    def getMaxKey(self) -> str:
        return self.left.next.val[0]

    def getMinKey(self) -> str:
        return self.right.prev.val[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
