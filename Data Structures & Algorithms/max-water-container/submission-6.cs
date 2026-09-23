/*
Input:
    - int[] : heights
Output:
    - int : max amoiunt of water a container can store
Constraints:
    - length of heights: [2,100000]
    - values of heights: [0,10000]

length = rightIndex - leftIndex
height = min(rightIndex, leftIndex)
Area = lengh * height

Plan: Two pointers
1. Create variables
    - maxArea = 0 
    - left = 0 
    - right = len(heights) - 1
2. while left < right:
        length = right - left
        height = min(right, left)
        area = length * height

        maxArea = max(maxArea, area)

        if leftIndex > rightIndex:
            decrement right
        else
            increment left 
3. Return maxArea
*/

public class Solution {
    public int MaxArea(int[] heights) {
        int maxArea = 0;
        int left = 0;
        int right = heights.Length - 1;

        while (left < right) { 
            int area = (right - left) * Math.Min(heights[left], heights[right]);
            maxArea = Math.Max(maxArea, area);

            // update pointers
            if (heights[left] > heights[right]) {
                right--;
            }
            else {
                left++;
            }
        }

        return maxArea;
    }
}
