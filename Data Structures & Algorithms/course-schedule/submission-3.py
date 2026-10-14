class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # output: returning a boolean if the prerequiste path is possible
        # so numCourses is just the number of courses given to us
        # looking at the test cases, if we find a loop, it'd fail
        # we can use depth first search, but on what?
        # we make an adjacency list -> use depth first search on that
        # bc we need direction, directed graph
        
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for prereq, course in prerequisites:
            preMap[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True

            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
                
        
        # if at anypoint dfs is false, return false
        for course in preMap:
            if not dfs(course):
                return False
        
        return True
