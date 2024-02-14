# 508. Most Frequent Subtree Sum
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        a = defaultdict(int)

        def dfs(cur):
            if not cur:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)
            res = left + right + cur.val
            a[res] += 1
            return res

        dfs(root)
        max_count = max(a.values())
        return [i for i in a if a[i] == max_count]
