# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create pointers to head of each linked list
        curr1 = list1
        curr2 = list2

        # create a temporary node to hold our result linked list
        dummy = ListNode(0, None)
        temp = dummy

        # iterate through both lists when there is a valid node
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1

                curr1 = curr1.next
            else:
                temp.next = curr2

                curr2 = curr2.next
            
            temp = temp.next

        # if one of the lists still have remaining elements, connect the remaining list
        if curr1:
            temp.next = curr1
        
        if curr2:
            temp.next = curr2

        return dummy.next

        
