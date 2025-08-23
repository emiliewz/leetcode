class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a / b = 2.0
        # b / c = 3.0
        
        # a/ c = ? 6 (a/b)*(b/c)
        # b / a = ? 0.5 (1 / (a/b))
        # a / a = ? 1
        
        # edge cases
        # a / e = -1
        # x / x = ? -1
        
        # use {a: {b: a/b, c: a/c} ; b: {a: b/a, c: b/c} ; c: {a: c/a, b: a/b}}
        
        graph = defaultdict(dict)
        # {}
        # [["a","b"],["b","c"]]
        for i, (u,v) in enumerate(equations):
            graph[u][v]=values[i] # u/v
            graph[v][u]=1/values[i] # v/u
            
        # a, b ,c -> ab, bc, ac
            
        for i in graph:
            graph[i][i] = 1
            for j, k in combinations(graph[i], 2):
                if j not in graph[k]:
                    graph[k][j] = graph[i][j]/graph[i][k]   # (i/j) / (i/k)
                    graph[j][k] = 1/graph[k][j]
        
        return [graph[u][v] if u in graph and v in graph[u] else -1 for u,v in queries]
                
        
        