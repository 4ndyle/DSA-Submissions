"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Input:
    - Node : head 
        int : val
        Node : next (could be None)
        Node : random (could be None)
Output:
    - Node : head of the copied linked list 
Constraints:
    - totals node: 0 <= n <= 100
    - range of values: -100 <= val <= 100
    - random can be None or a existing node in the list 

Plan: 
1. Create a new linked list with each node value and next pointers the same as the input linked list 
and create a dict to keep track of the values in each node (for pointing random pointer)
    for each node: 
        - copy the value and next pointers 
        - update the dict val, dict[currNode.val] = currNode

2. Do a second pass through the linked list and use the dict[nodeVal] to find the node to point to 
3. Return the head of the new linked list 
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a dict and map each old node to their new node value 
        nodeDict = {}

        curr = head

        while curr:
            # create a new node and add it to the dict with its respective old node 
            newNode = Node(curr.val)
            nodeDict[curr] = newNode

            curr = curr.next

        print(nodeDict)

        # traverse through the old linked list and connect each new node to their new node val
        oldCurr = head 

        while oldCurr:
            # find the new nodes in memory 
            currNewNode = nodeDict[oldCurr]
            nextNewNode = nodeDict[oldCurr.next] if oldCurr.next else None
            randomNewNode = nodeDict[oldCurr.random] if oldCurr.random else None

            # update pointer of each new node to their new next and random nodes
            currNewNode.next = nextNewNode
            currNewNode.random = randomNewNode

            oldCurr = oldCurr.next

        return nodeDict[head] if head else None




