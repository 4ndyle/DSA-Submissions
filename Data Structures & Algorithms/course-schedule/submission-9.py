"""
Input:
    - int : numCourses
    - List[List[int]] : prerequisites 
Output:
    - bool : true if all courses can be completed
Constraints:
    - [a,b] : course b MUST be taken before course a
    - possible lengths of prerequisites: [0,1000] 
    - possible values of prequisites: [0,numCourses]
    - prerequisite[i].length = 2
    - possible values of numCourses: [1,100]

Plan: Create an adjacency list and map each course to their prereq
{
    course : set(prerequisites)
}

Example 1:
{
    0 : set(1)
    1 : set(0)
}

Iterate through and check if course 0 needs course 1 and course 1 needs course 0

1. Create variables
    - courseMap = {}
2. for course, prereq in prerequisites:
        courseMap[course] = courseMap.get(course, set()).add(prereq)
3. for course, prereqList in courseMap:
        for prereq in prereqList:
            if course in courseMap[prereq]:
                return False
4. Return True
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list (adjacency list)
        courseMap = {i:set() for i in range(numCourses)}

        for course, prereq in prerequisites:
            courseMap[course].add(prereq)

        # go through adjacency list and check for a cycle
        visited = set()
        coursePossibility = {}

        def dfsHelper(node):
            if node in coursePossibility:
                return coursePossibility[node]
            if node in visited:
                return False

            # mark node as visited
            visited.add(node)

            for neighbor in courseMap[node]:
                if not dfsHelper(neighbor):
                    coursePossibility[node] = False
                    return False
            
            visited.remove(node)

            coursePossibility[node] = True
            return True

        for course in courseMap:            
            if not dfsHelper(course):
                return False
        
        return True
        
