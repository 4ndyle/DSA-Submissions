"""
Input:
    - ListNode : head 
OutputL
    - ListNode: reversed linked list or None if the linkedlist is empty 
Constraints:
    - range of values
    - length of linked list 

Example:
0 -> 1 -> 2 -> 3 

None <- 0

Plan:
1. Create a prev variable as a pointer to None 
2. Create a curr variable as a pointer to current position in linked list 
3. For each node in the linked list, point the node to the prev variable 
4. return prev variable (points to the reversed linked list head)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        # traverse through each node and point to prev value 
        while curr:
            # keep track of the next node in the original linked list 
            temp = curr.next 

            # reverse the direction of the current code and update the curr pointer to the next node in the original list  
            curr.next = prev 
            prev = curr 
            curr = temp

        return prev

