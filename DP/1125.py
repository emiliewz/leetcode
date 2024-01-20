# 1125. Smallest Sufficient Team
from typing import List


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        a = {0: []}
        n = len(req_skills)
        skills = {s: i for i, s in enumerate(req_skills)}

        for i, person in enumerate(people):
            prev_skills = 0
            for s in person:
                prev_skills |= 1 << skills[s]

            for s, p in list(a.items()):
                new_skills = s | prev_skills
                if not new_skills in a or len(a[new_skills]) > len(p) + 1:
                    a[new_skills] = p + [i]

        return a[(1 << n) - 1]


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        n = len(req_skills)
        dp = {0: []}
        skill_dict = {skill: i for i, skill in enumerate(req_skills)}

        for i, j in enumerate(people):
            prev_skills = 0
            for skill in j:
                prev_skills |= 1 << skill_dict[skill]

            for skills, team in list(dp.items()):
                new_skills = prev_skills | skills
                if not new_skills in dp or len(dp[new_skills]) > len(team) + 1:
                    dp[new_skills] = team + [i]

        return dp[(1 << n) - 1]
