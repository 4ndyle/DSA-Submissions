# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Input:
    - ListNode : head of linked list 
Output:
    - ListNode : head a reversed linked list from input
Edge Cases:
    - empty head -> None

Plan: Iterate through the linked list and point the current node's next pointer
to the previous node. 

Psuedo Code:
prev = None
curr = head

while curr:
    temp = curr

    curr.next = prev

    prev = curr
    curr = temp.next

return prev
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next

            curr.next = prev
            prev = curr

            curr = temp

        return prev