# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy 
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # calculate the sum and digits at ones/tenths place 
            nodeSum = val1 + val2 + carry

            onesPlace = nodeSum % 10

            tenthsPlace = nodeSum // 10
            carry = tenthsPlace 

            # set the result linked list node to the ones place value 
            temp.next = ListNode(onesPlace)
            temp = temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        
        return dummy.next 



