# 449. Serialize and Deserialize BST
from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        q, a = deque([(root, 0)]), defaultdict(list)
        a[0] = [str(root.val)]
        while q:
            cur, x = q.popleft()
            if cur.left:
                q.append((cur.left, x + 1))
                a[x + 1].append(str(cur.left.val))
            else:
                a[x + 1].append("n")
            if cur.right:
                q.append((cur.right, x + 1))
                a[x + 1].append(str(cur.right.val))
            else:
                a[x + 1].append("n")
        res = [",".join(j) for _, j in a.items()]
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))
        q = deque([root])
        while q:
            cur = q.popleft()
            left = data.popleft()
            right = data.popleft()
            if left != "n":
                cur.left = TreeNode(int(left))
                q.append(cur.left)
            if right != "n":
                cur.right = TreeNode(int(right))
                q.append(cur.right)

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
