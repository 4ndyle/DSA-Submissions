/*
Input:
    - int[] : nums
    - int : target
Output:
    - int : index of the target, otherwise -1 if not found 

Constraints:
    - O(logn) time 
    - sorted in ascending order 

Plan: 
1. Linear scan - O(n)
2. Binary Search - O(log n)

*/

public class Solution {
    public int Search(int[] nums, int target) {
        // two pointers for search range 
        int left = 0;
        int right = nums.Length - 1;

        // perform binary search
        while (left <= right) {
            // find the middle element 
            int mid = (int)Math.Floor((double)(left + right) / 2);

            // check if the middle element = target
            if (target == nums[mid]) {
                return mid;
            }

            // search left if target < middle element
            if (target < nums[mid]) {
                right = mid - 1;
            }
            // search right if target > middle element
            else {
                left = mid + 1;
            }
        }

        return -1;
    }
}
