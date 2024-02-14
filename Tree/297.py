# 297. Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
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

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
