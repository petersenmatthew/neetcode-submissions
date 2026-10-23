class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                        
        preMap = {}
        
        for pair in prerequisites:
            if pair[0] not in preMap:
                preMap[pair[0]] = []

            preMap[pair[0]].append(pair[1])

        visited = set()

        def dfs(n):
            if n in visited:
                return False
            
            prereqs = preMap.get(n, [])
            if len(prereqs) == 0:
                return True

            visited.add(n)

            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            preMap[n] = []
            visited.remove(n)
            return True
                
        
        for course in preMap:
            if not dfs(course):
                return False
            
        return True        
            