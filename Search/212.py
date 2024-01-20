# 212. Word Search II
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, root):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in root:
                return
            letter = board[i][j]
            cur = root[letter]
            # word = cur.pop('#', False)
            if "#" in cur:
                res.append(cur.pop("#"))
            # if word:
            #     res.append(word)

            board[i][j] = 0
            dfs(i + 1, j, cur)
            dfs(i - 1, j, cur)
            dfs(i, j + 1, cur)
            dfs(i, j - 1, cur)
            board[i][j] = letter
            if not cur:
                root.pop(letter)
            return res

        m, n = len(board), len(board[0])
        res = []
        a = {}

        for word in words:
            cur = a
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur["#"] = word

        for i in range(m):
            for j in range(n):
                if board[i][j] in a:
                    dfs(i, j, a)

        return res


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, k, word):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = 0
            res = (
                dfs(i + 1, j, k + 1, word)
                or dfs(i - 1, j, k + 1, word)
                or dfs(i, j + 1, k + 1, word)
                or dfs(i, j - 1, k + 1, word)
            )
            board[i][j] = word[k]
            return res

        m, n = len(board), len(board[0])
        res = []
        a = {}

        for word in words:
            a.setdefault(word[0], []).append(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] in a:
                    all_words = a[board[i][j]]
                    for word in all_words[:]:
                        if dfs(i, j, 0, word):
                            res.append(word)
                            if len(all_words) > 1:
                                a[board[i][j]].remove(word)
                            else:
                                a.pop(board[i][j])

        return res


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
