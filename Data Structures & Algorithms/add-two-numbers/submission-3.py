# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Input
    - ListNode: L1
    - ListNode: L2
Output:
    - ListNode: the sum of the two numbers as a linked list 

Notes:
    - Digits are stored in reverse order 
    - no leading zeroes in digits 

Example: 

1 -> 2 -> 3 (321)
4 -> 5 -> 6 (654)
-----------------
5 -> 7 -> 9 (975)

1
  9
+ 9
-----
 18

11
341
659 + 
--------
900

 1
341
009 + 
------
350

There will be a carry over when the sum of 2 digits >= 10
    1. Determine when the sum is >= 10
    2. sum // 10 = carry over 
    3. number to move down = ones place = remainder after division by 10 = sum % 10

Example:
18
18 // 10 = 1
18 % 10 = 8

carry over = 1
number to move down = 8

Plan: 
1. Create a dummy node to store the resulting sum
2. Traverse through both linked lists and calculate the sum of the current nodes
    - if there is a carry over, keep track of the carry over and add it into the sum of the next nodes
3. Return dummy.next
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to store the resulting sum 
        dummy = ListNode(0)
        dummyCurr = dummy

        # Traverse through both the linked lists and calculate their sum
        curr1 = l1
        curr2 = l2
        carry = 0 

        while curr1 or curr2 or carry:
            # find the values of both nodes and their sum (set to 0 if one of the nodes are empty)
            num1 = curr1.val if curr1 else 0
            num2 = curr2.val if curr2 else 0

            currSum = num1 + num2 + carry

            # calcualte the carry over (if any) and the ones place 
            onesPlace = currSum % 10
            carry = currSum // 10

            # create a new node for the current position and connect to the resulting linked list 
            newNode = ListNode(onesPlace)

            dummyCurr.next = newNode

            # update pointers
            dummyCurr = dummyCurr.next
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        return dummy.next







        