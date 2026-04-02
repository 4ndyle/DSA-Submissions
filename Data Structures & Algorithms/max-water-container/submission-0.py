class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use left and right pointers for start and end
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            # calculate area between two integers and set max
            height = min(heights[left],heights[right])
            length = right - left
            area = length * height

            maxArea = max(maxArea, area)
            
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea