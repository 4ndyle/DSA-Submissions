# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
input: linked list
output: linked list (reordered)

Plan:
1. Use a fast and slow pointer to traverse through the linked list and find the middle. Slow will be at the middle
2. Reverse the second half of the linked list, starting at the middle to the end. 
3. After the second half is reversed, use two pointers to create the reordered list

Find the second half
slow = head
fast = head.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

Reverse the second half
currSecond = slow.next
slow.next = None
prev = None

while currSecond:
    temp = currSecond.next
    currSecond.next = prev
    currSecond = temp

Use two pointers to create new order
left = head
right = prev

while right:
    temp1, temp2 = left, right
    left.next = right
    right.next = temp1.next
    left, right = temp1.next, temp2.next
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the second half
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        currSecond = slow.next
        slow.next = None
        prev = None

        while currSecond:
            temp = currSecond.next
            currSecond.next = prev
            
            prev = currSecond
            currSecond = temp

        # # Use two pointers to create new order
        left = head
        right = prev

        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1

            left, right = temp1, temp2

            




