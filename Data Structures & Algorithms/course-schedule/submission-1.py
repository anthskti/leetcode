class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # our output is a boolean: returning the possibility of finishing all the courses. 
        # are numCourses == to the number of courses present?
        # We can view this problem like a graph. from a direct edge from node a to b. 
        # if we find a cycle, we'd return false

        # approach: we can utilize dfs; and if a node is already read, a cycle is is found. so return false. 

        # we just need to build the graph from courses that do not need prerequisites.

        # we could build an adjacency list

        pre_map = {}
        for i in range(numCourses):
            pre_map[i] = []
        
        for a, b in prerequisites:
            pre_map[a].append(b)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if pre_map[course] == []:
                return True
            
            visited.add(course)
            for p in pre_map[course]:
                if not dfs(p): 
                    return False

            visited.remove(course)
            pre_map[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course): 
                return False

        return True
