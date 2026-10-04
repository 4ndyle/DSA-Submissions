# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currL1 = list1
        currL2 = list2

        dummy = ListNode()
        head = dummy

        # alternatively add nodes to result linkedlist based on values 
        while currL1 and currL2:
            if currL1.val <= currL2.val:
                dummy.next = currL1
                currL1 = currL1.next
            else:
                dummy.next = currL2
                currL2 = currL2.next

            dummy = dummy.next

        # attach remainder of list 
        while currL1:
            dummy.next = currL1
            dummy = dummy.next 

            currL1 = currL1.next

        while currL2:
            dummy.next = currL2
            dummy = dummy.next

            currL2 = dummy.next

        return head.next