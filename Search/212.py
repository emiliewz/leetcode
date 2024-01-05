# 212. Word Search II
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        r, c = len(board), len(board[0])
        visit, res = set(), set()

        def dfs(x, y, node, word):
            if (
                x < 0
                or y < 0
                or x == r
                or y == c
                or (x, y) in visit
                or board[x][y] not in node.children
            ):
                return

            visit.add((x, y))
            node = node.children[board[x][y]]
            word += board[x][y]
            if node.isWord:
                res.add(word)
            dfs(x + 1, y, node, word)
            dfs(x - 1, y, node, word)
            dfs(x, y + 1, node, word)
            dfs(x, y - 1, node, word)
            visit.remove((x, y))

        for i in range(r):
            for j in range(c):
                dfs(i, j, root, "")
        return list(res)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        r = len(board)
        c = len(board[0])

        def dfs(x, y, i, word):
            if i == len(word):
                res.append(word)
                return True
            if x < 0 or y < 0 or x >= r or y >= c or word[i] != board[x][y]:
                return False
            cur = board[x][y]
            board[x][y] = 0
            result = (
                dfs(x + 1, y, i + 1, word)
                or dfs(x - 1, y, i + 1, word)
                or dfs(x, y - 1, i + 1, word)
                or dfs(x, y + 1, i + 1, word)
            )
            board[x][y] = cur
            return result

        def findWord(word):
            for i in range(r):
                for j in range(c):
                    if dfs(i, j, 0, word):
                        return True

        for word in words:
            findWord(word)

        return res
