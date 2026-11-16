from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map prereq list to adjacency list
        # count the in-degrees of each node
        indeg = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1
        
        # add nodes with degree 0 to qeueu
        queue = deque()

        for course, indegree in indeg.items():
            if indegree == 0:
                queue.append(course)

        # Kahns Algorithm
        order = [] 

        while queue:
            node = queue.popleft()
            order.append(node)

            # decrement in-degree of current node neighbors
            for neighbor in adj[node]:
                indeg[neighbor] -= 1

                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        return len(order) == numCourses

        