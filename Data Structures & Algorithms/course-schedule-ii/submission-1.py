class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}

        for pair in prerequisites:
            if pair[0] not in preMap:
                preMap[pair[0]] = []
            preMap[pair[0]].append(pair[1])
        completed = set()
        # adjacency list
        output = []
        def dfs(course, visited_set):
            if course in completed:
                return True
            if course in visited_set:
                return False
            
            #check for cycles
            visited_set.add(course)
            for prereq in preMap.get(course, []):
                if not dfs(prereq, visited_set):
                    return False
            
            # this course is valid to be taken :)
            visited_set.remove(course)
            completed.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return []

        return output
        