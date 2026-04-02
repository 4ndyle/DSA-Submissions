# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node for keeping track of the list 
        dummy = ListNode(0)
        dummy.next = head

        # find the length of the list 
        length = 0
        curr = head 

        while curr:
            length += 1
            curr = curr.next

        print(f"length = {length}")

        # calculate the nth node 
        nodeToRemove = length - n
        print(f"removing the node ta index {nodeToRemove}")

        # traverse through the list and remove the node at the nodeToRemove index 
        index = 0 
        prev = dummy
        curr = head 

        while curr:
            if nodeToRemove == index:
                prev.next = curr.next 
                break

            prev = curr
            curr = curr.next
            index += 1

        return dummy.next         



