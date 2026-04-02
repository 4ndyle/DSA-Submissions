"""
Input:
    - List[int] : heights where heights[i] represents the height of the ith bar
Output:
    - int : max amount of water (area) between any two bars

Example 1: 
height = min(left bar, right bar)
length = right - left 
waterArea = height * length

Plan:
Use two pointers and move pointers towards middle of the bucket to calculate the water. 
    - Move the pointer with the lower height at each iteration (to find the max area)
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # create variable to keep track of maxWater and pointers
        maxWater = 0 

        left = 0
        right = len(heights) - 1

        while left < right:
            # calculate the area of the current iteration
            height = min(heights[left], heights[right])
            length = right - left

            waterArea = height * length
            maxWater = max(waterArea, maxWater)

            # update the pointers depending on heights 
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxWater



