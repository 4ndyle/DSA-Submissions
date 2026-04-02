# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the length of the linked list
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        print(f"length {length}")

        # Iterate to the nth node from the end of the list 
        nodeIndex = length - n
        currIndex = 0

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if currIndex == nodeIndex:
                # remove node from list 
                print(f"Remove node {curr.val}")
                prev.next = curr.next
                break
            
            prev = curr
            curr = curr.next
            currIndex += 1

        return dummy.next

        
