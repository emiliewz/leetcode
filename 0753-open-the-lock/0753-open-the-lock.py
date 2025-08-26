class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        def getNeighbor(lock):
            res = []
            for i in range(4):
                res.append(lock[:i] + str((int(lock[i])+1+10)%10) + lock[i+1:])
                
                res.append(lock[:i] + str((int(lock[i])-1+10)%10) + lock[i+1:])
            return res
            
            
        queue = deque()
        queue.append('0000')
        visited = set(deadends)
        visited.add('0000')
        steps = 0

        
        while queue:
            
            for _ in range(len(queue)):
                cur = queue.popleft()
            
                if cur == target:
                    return steps
                
                for neighbor in getNeighbor(cur):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            steps += 1
        return -1