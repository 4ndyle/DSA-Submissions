# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Input: 
    - ListNode : number represented as a linked list 
    - ListNode : number represented as a linked list 
    123 = 3 -> 2 -> 1 -> 
Output: 
    - ListNode : sum of the two numbers as a linked list 

321
654 + 
-------- 
975

 321
 854 + 
--------
1175 = 5 -> 7 -> 1 -> 1

If we get a number > 9, then
current node = ones place value 
next node = l1 node + l2 node + carry OR if next node doesn't exist, then next node = carry
 1
 371
 654 + 
--------
1025 = 5 -> 2 -> 0 -> 1

 371
   4 + 
--------
375 = 5 -> 7 -> 3

Plan: 
1. Iterate though both linked lists and add their current nodes together
    - if sum <= 9, create a new node to represent their sum in that positon
    - if sum > 9:
        - no next node: 
            - current node = ones place 
            - next node = tenths place
        - next node:
            - current node = ones place 
            - next node = l1 node + l2 node + carry over 
2. If one of the linked lists is longer, connect the remaining digits to the linked list result 
"""         

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        # Iterate through both linked lists and calculate their sum 
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 and curr2:
            nodeSum = curr1.val + curr2.val + carry
            carry = 0

            if nodeSum <= 9:
                temp.next = ListNode(nodeSum)
            else:
                # will have carry over 
                onesPlace = nodeSum % 10
                print(f"ones place is {onesPlace}")
                tenthsPlace = nodeSum // 10

                temp.next = ListNode(onesPlace)
                carry = tenthsPlace 

            temp = temp.next
            curr1 = curr1.next
            curr2 = curr2.next

        # if one of the numbers is longer than the other 
        while curr1:
            nodeSum = curr1.val + carry
            carry = 0

            if nodeSum <= 9:
                temp.next = ListNode(nodeSum)
            else:
                # will have carry over 
                onesPlace = nodeSum % 10
                tenthsPlace = nodeSum // 10

                temp.next = ListNode(onesPlace)
                carry = tenthsPlace 

            temp = temp.next
            curr1 = curr1.next

        while curr2:
            nodeSum = curr2.val + carry
            carry = 0

            if nodeSum <= 9:
                temp.next = ListNode(nodeSum)
            else:
                # will have carry over 
                onesPlace = nodeSum % 10
                tenthsPlace = nodeSum // 10

                temp.next = ListNode(onesPlace)
                carry = tenthsPlace 

            temp = temp.next
            curr2 = curr2.next

        if carry:
            temp.next = ListNode(carry)
            temp = temp.next

        return dummy.next



                















