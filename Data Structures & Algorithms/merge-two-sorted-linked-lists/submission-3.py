# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
input: two lists ()
output: one linked list of the two lists sorted 
constraints: 
edge cases:
    - one empty list: return other list
    - two empty lists: return empty list

Plan:
High level: Create two pointers for each list and check the value of the pointer at each list and add them to the new linked list based on their value. 

temp = ListNode(0, None)
res = temp
curr1 = list1
curr2 = list2

while curr1 and curr2:
    if curr1.val <= curr2.val:
        res.next =  curr1
    else:
        res.next = curr2

    res = res.next

if not curr1:
    res.next = curr2
if not curr2:
    res.next = curr1

return temp.next
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, None)
        res = temp
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next

            res = res.next

        if not curr1:
            res.next = curr2
        if not curr2:
            res.next = curr1

        return temp.next



