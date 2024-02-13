# 1125. Smallest Sufficient Team
from typing import List


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        skills, a, n = (
            {j: i for i, j in enumerate(req_skills)},
            {0: []},
            len(req_skills),
        )
        complete = 1 << n

        for person, skill in enumerate(people):
            cur_mask = 0
            for s in skill:
                cur_mask |= 1 << skills[s]
            for prev_mask, team in list(a.items()):
                mask = cur_mask | prev_mask
                if mask not in a or len(a[mask]) > len(team) + 1:
                    a[mask] = team + [person]

        return a[complete - 1]
