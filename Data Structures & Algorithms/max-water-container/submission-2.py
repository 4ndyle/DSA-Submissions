"""
Input: array (heights)
Output: integer (maximum amount of water a container can store)
Constraints:
    - any two bars form a container 
Edge Cases:
    - empty list -> 0
    - list of one element? -> 0

Plan: Use two pointers, one at start and one at end. Move one of the pointers
if the current height of the bar is less than the other bar. Keep track of max area (height * length)

Intialize two pointers (left and right)
Create a variable to keep track of the max area

while left < right:
    calculate the current area (length(right-left) * min(left/right bar))
    if current area > max area, set max area as current area

    if left bar > right bar:
        move right bar towards middle
    otherwise:
        move left bar towards middle

return max area
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxArea = 0

        while left < right:
            length = right - left
            height = min(heights[left], heights[right])
            area = length * height

            maxArea = max(maxArea, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea
