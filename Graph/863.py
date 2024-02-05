# 863. All Nodes Distance K in Binary Tree
from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        par = {}
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                par[cur.left.val] = cur
                q.append(cur.left)
            if cur.right:
                par[cur.right.val] = cur
                q.append(cur.right)

        q.append(target)
        visit = set()
        res = []
        while q and k >= 0:
            for _ in range(len(q)):
                cur = q.popleft()
                visit.add(cur.val)
                if k == 0:
                    res.append(cur.val)

                if cur.val in par and par[cur.val].val not in visit:
                    q.append(par[cur.val])
                if cur.left and cur.left.val not in visit:
                    q.append(cur.left)
                if cur.right and cur.right.val not in visit:
                    q.append(cur.right)
            k -= 1

        return res


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = deque([root])
        trees = {}

        while q:
            cur = q.popleft()
            if cur.left:
                trees[cur.left.val] = cur
                q.append(cur.left)
            if cur.right:
                trees[cur.right.val] = cur
                q.append(cur.right)

        q.append(target)
        visit = set()

        while k > 0 and q:
            for _ in range(len(q)):
                cur = q.popleft()
                visit.add(cur.val)
                if cur.left and cur.left.val not in visit:
                    q.append(cur.left)
                if cur.right and cur.right.val not in visit:
                    q.append(cur.right)
                if cur.val in trees and trees[cur.val].val not in visit:
                    q.append(trees[cur.val])
            k -= 1
        res = []
        while q:
            res.append(q.popleft().val)

        return res
