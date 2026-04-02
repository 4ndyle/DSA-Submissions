"""
Input:
    - ListNode : head
Output:
    - None : modify the input linked list in place 

General Case:
[0, n-1, 1, n-2, 2, n-3, ...]

Plan: 
1. Find the middle of the linked list and mark it 
2. Iterate to the end of the linked list from the middle and reverse the second half of the linked list 
3. Create 2 pointers at the head of each linked list and connect them alternatively in the correct order 

2 -> 4 -> 6 -> None | None <- 8 <- 10
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the linked list 
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # print(slow.val)

        # Reverse the second half of the linked list 
        curr = slow.next 
        slow.next = None 

        prev = None

        while curr:
            nextNode = curr.next 

            curr.next = prev 
            prev = curr

            curr = nextNode 

        # Connect each node in the linked lists in alternative order according to the general case 
        curr1 = head
        curr2 = prev 

        while curr1 and curr2: 
            # keep track of next nodes
            curr1NextNode = curr1.next
            curr2NextNode = curr2.next

            # connect the nodes 
            curr1.next = curr2
            curr2.next = curr1NextNode 

            curr1 = curr1NextNode
            curr2 = curr2NextNode

