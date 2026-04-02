"""
Input:
    - ListNode : list1
    - ListNode : list2
Output:
    - ListNode : merged list of list1 and list2

Plan:
1. Create a pointer for the head of each linked list
2. While both nodes are valid, connect the node that is less than the other (in ascending order)
3. Check if any nodes are are not connected, and connect it to the end of the resulting linked list
4. Return the head of the new linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a node pointing to the res
        dummy = ListNode(0)
        curr = dummy

        # Create a pointer for each linked list
        l1Curr = list1
        l2Curr = list2

        # alternatively connect the nodes of each list based on their values (ascending order)
        while l1Curr and l2Curr:
            if l1Curr.val < l2Curr.val:
                curr.next = l1Curr
                l1Curr = l1Curr.next
            else:
                curr.next = l2Curr
                l2Curr = l2Curr.next
            
            # update general current pointer for dummy linked list 
            curr = curr.next

        # check if any linked lists have remaining elements and connect them
        if l1Curr:
            curr.next = l1Curr
        
        if l2Curr:
            curr.next = l2Curr
        
        return dummy.next