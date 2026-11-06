class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}

        def dfs(course, visited_set):
            if course not in preMap or len(preMap[course]) == 0:
                return True
            if course in visited_set:
                return False
            
            visited_set.add(course)
            # need to check for cycles
            for prereq in preMap[course]:
                if not dfs(prereq, visited_set):
                    return False
            visited_set.remove(course)
            preMap[course] = []
            return True

        
        for pair in prerequisites:
            if pair[0] not in preMap:
                preMap[pair[0]] = []
            preMap[pair[0]].append(pair[1])
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True
        # now have an adjancecy list

        # how to check if a course can be completed?
        # base case: no pointers outwards
        # recursively check its children (its prereqs)