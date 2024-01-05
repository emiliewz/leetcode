# 126. Word Ladder II
from typing import DefaultDict, Deque, List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        nei_d = DefaultDict(list)
        for word in wordList:
            for i in range(0, len(word)):
                nei_d[word[0:i] + "*" + word[i + 1 :]].append(word)

        graph = {beginWord: []}
        q = Deque([beginWord])
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
