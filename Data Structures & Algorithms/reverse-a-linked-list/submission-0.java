/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        ListNode tmp = null;

        // while current pointer is not null, set temp as current and move current
        // temp's next is equal to the previous
        while(curr != null) {
            tmp = curr;
            curr = curr.next;
            tmp.next = prev;
            prev = tmp;
        }

        // once curr is at null, prev points to the last node of the list
        head = prev;

        return head;
    }
}
