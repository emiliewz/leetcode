# 433. Minimum Genetic Mutation
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([startGene])
        visit = set([startGene])
        mut = 0

        def canMutate(gene, cur):
            diff = 0
            i = 0
            while i < 8:
                if gene[i] != cur[i]:
                    diff += 1
                    if diff > 1:
                        return False
                i += 1
            return True

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return mut
                for gene in bank:
                    if gene not in visit:
                        if canMutate(gene, cur):
                            q.append(gene)
                            visit.add(gene)

            mut += 1

        return -1


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([startGene])
        visit = set([startGene])
        mut = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return mut
                for gene in bank:
                    if gene not in visit:
                        for i in range(8):
                            if gene[:i] == cur[:i] and gene[i + 1 :] == cur[i + 1 :]:
                                q.append(gene)
                                visit.add(gene)

            mut += 1

        return -1


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([startGene])
        visit = set([startGene])
        mut = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return mut
                for i in range(8):
                    for gene in bank:
                        if (
                            gene not in visit
                            and gene[:i] == cur[:i]
                            and gene[i + 1 :] == cur[i + 1 :]
                        ):
                            q.append(gene)
                            visit.add(gene)

            mut += 1

        return -1
