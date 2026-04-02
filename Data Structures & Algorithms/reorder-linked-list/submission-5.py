# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Input:  
    - ListNode : head of a linked list
Output:
    - ListNode : reordered linked list 

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle element of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # reverse the second half of the list
        
        curr = slow.next
        slow.next = None

        prev = None

        while curr:
            temp = curr.next

            curr.next = prev

            prev = curr
            curr = temp


        # iterate through both linked lists and add each node alternatively to the result
        curr1 = head
        curr2 = prev

        while curr2:
            temp1next = curr1.next
            temp2next = curr2.next

            curr1.next = curr2
            curr2.next = temp1next

            curr1 = temp1next
            curr2 = temp2next

        

        