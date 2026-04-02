# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        queue = deque()
        queue.append(root)

        visited = []

        while queue:
            currentQueueLength = len(queue)

            # go through all nodes on the current queue (which are all on the same level)
            currentLevel = []
            for i in range(currentQueueLength):
                node = queue.popleft()
                
                if node:
                    currentLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if currentLevel:
                visited.append(currentLevel)
                
        return visited