# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
input: head (of a linked list)
output: head (of a linked list that is reversed of the input)
edge cases:
    - empty list: return empty 
    - list of one element: returning one element

High level: Temporary head pointer to keep track of the previous node of the current node. 
As we iterate through the list, set the next of the current node to the previous node.

Overview:
Set a node (represents prev node), set current node to head

while current node is not None: 
    use a temp node to represent the next node of the current pointer (so we dont lose it)

    set the current node's next to the prev node
    set the prev node to the current node

    set the current node to the temp node (allows us to keep iterating)

return temp
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current: 
            temp = current.next

            current.next = prev
            prev = current
            
            current = temp

        return prev