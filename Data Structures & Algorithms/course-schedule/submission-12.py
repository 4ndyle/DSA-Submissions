from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = {i:set() for i in range(numCourses)}
        
        # convert prerequisites into adjacency list 
        for course, prereq in prerequisites:
            courseToPrereq[course].add(prereq)

        # go through adjacency list and check for cycle 
        visited = set()

        def dfs(course):
            # base case 
            if course in visited:
                return False

            if len(courseToPrereq[course]) == 0:
                return True

            # mark course as visited 
            visited.add(course)

            # go through prerequisites
            for prereq in courseToPrereq[course]:
                if not dfs(prereq):
                    return False 
            
            visited.remove(course)
            courseToPrereq[course] = set()
            return True

        for course in courseToPrereq:
            if not dfs(course):
                return False 

        return True 




