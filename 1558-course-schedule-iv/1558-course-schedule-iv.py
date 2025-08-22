class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        allPrereq = defaultdict(set)
        indeg = [0] * numCourses
        
        for prereq, course in prerequisites:
            graph[prereq].add(course)
            indeg[course] += 1
        
        independent = [i for i in range(numCourses) if not indeg[i]]
        q = deque(independent)
        
        while q:
            cur = q.popleft()
            
            for c in graph[cur]:
                allPrereq[c].add(cur)
                allPrereq[c].update(allPrereq[cur])
                indeg[c] -= 1
                
                if not indeg[c]:
                    q.append(c)
        
        return [u in allPrereq[v] for u,v in queries]
        
            
            
        # course graph : {prereq: [next courses]}
        # iterate thru the queries
        #   [1, 0]
        #   
        # course_graph = defaultdict(list)
        # for prereq, course in prerequisites:
        #     course_graph[prereq].append(course)
            
        # ans = [False] * len(queries)
        # for prereq, course in queries:
        #     if course in course_graph[prereq]:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        
        # return ans
        
        
            
            
        '''
        class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                isPrereq[neighbor].add(node)
                isPrereq[neighbor].update(isPrereq[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return [u in isPrereq[v] for u, v in queries]
        '''
            
            