# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input:
    - TreeNode: root 
Output:
    - bool : whether or ont the tree is height balanced 
Constraints:
    - number of nodes: [0,1000]
    - range of values: [-1000,1000]

plan:
DFS Post-Order Traversal (Bottom Up)

[subtreeBalanced, depth]
def dfsHelper(root) -> [bool, int]:
    Base Case:
    if the root is empty, return [T, 0]

    Call recursive functions:
    dfsHelper(root.left)
    dfsHelper(root.righjt)

    Process the current node:
    if both subtrees are not balanced:
        return [max(leftDepth, rightDepth), False]

    Find the height difference of subtrees
    heightDifference = abs(leftDepth - rightDepth)

    if the height is more than 1:
        return [max(leftDepth, rightDepth), False]

    return [max(leftDepth, rightDepth)]

"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # define a helper function to traverse through tree
        def dfsHelper(root) -> (int, bool): 
            # base case
            if not root:
                return (0, True)

            # call the left and right subtrees 
            left = dfsHelper(root.left)
            right = dfsHelper(root.right)

            # process the current node
            # if either the left or right are not balanced, return false
            if not left[1] or not right[1]:
                return (max(left[0], right[0]) + 1, False)

            # if the height difference of left or right > 1, return False
            heightDifference = abs(left[0] - right[0])

            if heightDifference > 1: 
                return (max(left[0], right[0]) + 1, False)

            return [max(left[0], right[0]) + 1, True]

        res = dfsHelper(root)
        print(res)

        return res[1]








