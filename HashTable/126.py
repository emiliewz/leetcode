# 126. Word Ladder II
from collections import deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        a = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                a.setdefault(pattern, []).append(word)
        print(a)
        graph = {beginWord: []}

        def bfs():
            q = deque()
            q.append(beginWord)
            find = False

            while q and not find:
                cur = {}
                for _ in range(len(q)):
                    w = q.popleft()
                    if w == endWord:
                        find = True

                    for i in range(len(w)):
                        p = w[:i] + "*" + w[i + 1 :]
                        for word in a[p]:
                            if word not in graph:
                                if word not in cur:
                                    q.append(word)
                                cur.setdefault(word, []).append(w)
                graph.update(cur)
            return find

        def dfs(cur, w):
            if graph[w] == []:
                res.append(cur[::-1])
                return

            for word in graph[w]:
                dfs(cur + [word], word)

        res = []
        find = bfs()
        if not find:
            return []
        dfs([endWord], endWord)
        return res
