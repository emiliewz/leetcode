class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        visited = set()
        res = set()
        
        for i in range(len(s) - 9):
            curr_window = s[i:i + 10]
            if curr_window in visited:
                res.add(curr_window)
            else:
                visited.add(curr_window)
        return list(res)
            
        
        
     