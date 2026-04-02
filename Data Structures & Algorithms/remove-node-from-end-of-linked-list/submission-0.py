# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
input: linked list head 
output: linked list head (with removed element)

Plan: 
High Level: Create a pointer at the head and go through the list all the way to the end to get the total number of nodes.
Then with the total number of nodes, calculate how many steps it would take to get the the nth from last node using the total - n. 
total - n = index we are looking to remove 
ex 1: 4 - 2 = 2 (remove element at index 2)
ex 3: 2 - 2 = 0 (remove lement at index 0)
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the list
        curr = head
        length = 0

        while curr: 
            length += 1
            curr = curr.next
        
        print(f"total length = {length}")

        indexToRemove = length - n

        if n > length: 
            return head

        temp = ListNode(0, head)
        prev = temp
        curr = head 
        currIndex = 0

        while curr:
            if currIndex == indexToRemove:
                prev.next = curr.next
                break
            
            prev = curr
            curr = curr.next
            currIndex += 1

        return temp.next

            



