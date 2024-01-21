# 127. Word Ladder
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        a = {}
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                a.setdefault(pattern, []).append(word)

        q = deque()
        q.append(beginWord)
        res, visit = 1, set([beginWord])

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1 :]
                    for word in a[pattern]:
                        if word not in visit:
                            visit.add(word)
                            q.append(word)
            res += 1
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        nei = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                nei.setdefault(pattern, []).append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
