# 126. Word Ladder II
from collections import deque
from typing import DefaultDict, List


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


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        if endWord not in wordList:
            return []

        a = {}
        if beginWord not in wordList:
            wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1 :]
                a.setdefault(pattern, []).append(w)
        graph = {beginWord: []}

        def bfs():
            q = deque()
            q.append(beginWord)
            words = 1
            find = False

            while q and not find:
                cur = {}
                for _ in range(len(q)):
                    w = q.popleft()
                    if w == endWord:
                        find = True

                    for i in range(len(w)):
                        pattern = w[:i] + "*" + w[i + 1 :]
                        for word in a[pattern]:
                            if word not in graph:
                                if word not in cur:
                                    q.append(word)
                                cur.setdefault(word, []).append(w)

                words += 1
                graph.update(cur)
            return words - 1 if find else 0

        def dfs(cur, k):
            w = cur[-1]
            if k == 0:
                res.append(cur[::-1])
                return
            for word in graph[w]:
                dfs(cur + [word], k - 1)

        res = []
        k = bfs()
        if k == 0:
            return []
        dfs([endWord], k - 1)
        return res


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        nei_d = DefaultDict(list)
        for word in wordList:
            for i in range(0, len(word)):
                nei_d[word[0:i] + "*" + word[i + 1 :]].append(word)

        graph = {beginWord: []}
        q = deque([beginWord])
        go_on = True

        while q and go_on:
            curList = {}
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(0, len(cur)):
                    for nei_word in nei_d[cur[0:i] + "*" + cur[i + 1 :]]:
                        if nei_word == endWord:
                            go_on = False
                        if nei_word not in graph:
                            if nei_word not in curList:
                                curList[nei_word] = [cur]
                                q.append(nei_word)
                            else:
                                curList[nei_word].append(cur)
            graph.update(curList)

        res = []

        def dfs(cur, w):
            cur = cur + [w]
            if graph[w] == []:
                res.append(list(cur[::-1]))
                return
            for i in graph[w]:
                dfs(cur, i)

        if endWord in graph:
            dfs([], endWord)
        else:
            return []

        return res
