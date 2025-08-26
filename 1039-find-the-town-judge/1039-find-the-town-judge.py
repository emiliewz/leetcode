class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        candidates = set([i for i in range(1, n+1)])
        
        # if len(trust) != n-1:
        #     return -1
        
        for a, b in trust:
            graph[b].add(a)
            if a in candidates:
                candidates.remove(a)
            
        if (not candidates) or len(candidates) > 1:
            return -1
        
        judge_candidate = candidates.pop()
        
        if len(graph[judge_candidate]) == n-1:
            return judge_candidate
            
        return -1
            
            
            
            
            