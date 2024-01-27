# 990. Satisfiability of Equality Equations
from collections import defaultdict
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = defaultdict(set)
        inequal = defaultdict(set)

        for i in equations:
            a, b = i[0], i[-1]
            match = i[1] == "="
            if match:
                equal[a].add(b)
                equal[b].add(a)
            else:
                if a == b:
                    return False
                inequal[a].add(b)
                inequal[b].add(a)

        for k in equal:
            for i in equal[k]:
                for j in equal[k]:
                    if j not in equal[i]:
                        equal[i].add(j)

        for a, b in equal.items():
            for c in b:
                if c in inequal[a]:
                    return False

        return True
