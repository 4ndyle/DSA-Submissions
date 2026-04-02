"""
Input:
    - TreeNode : root
Output:
    - bool : whether or not the tree is balanced 

balanced: left and right subtrees of every node differ in height by no more than 1

Edge Case:
    - empty node : True 

Approaches: 
1. Use a dfs to iterate through every node and compare the height of the left and right subtrees (O(n^2))

2. Use dfs to calculate the height and balanced bool of every node 
    - return value: [height, isBalanced]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # base case: empty node 
            if not root:
                return [0,True]

            left = dfs(root.left)
            right = dfs(root.right)

            # balanced when: difference height of left and right <= 1 and left/rigght subtrees are balanced
            isBalancedBool = abs(left[0] - right[0]) <= 1 and left[1] and right[1]

            # return value: [height, isBalanced]
            return [max(left[0],right[0]) + 1, isBalancedBool]

        res = dfs(root)
        return res[1]