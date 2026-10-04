# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Plan: 
dummy = ListNode 
currRes = dummy
carryOver = 0

while curr1 or curr2:
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0

    sum = val1 + val2 + carryOver 
    carryOver = 0

    if sum >= 10:
        sum = sum % 10
        carryOver = 1

    add node to result 
    currRes.next = ListNode(sum)
    currRes = currRes.next

    update pointers 
    curr1 = curr1.next if curr1 else None 
    curr2 = curr2.next if curr2 else None 

return dummy.next
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        dummy = ListNode()
        currRes = dummy

        carryOver = 0 

        while curr1 or curr2 or carryOver > 0:
            # calculate the sum of two current nodes
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            currSum = val1 + val2 + carryOver
            carryOver = 0

            if currSum >= 10:
                currSum = currSum % 10
                carryOver = 1

            # add new node with currSum to result
            currRes.next = ListNode(currSum)

            # update pointers
            currRes = currRes.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        return dummy.next



        