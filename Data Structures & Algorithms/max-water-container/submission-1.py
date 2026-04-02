class Solution:
    '''
    Container represents the area between two bars 
    length = distance between the two bars
    height = minimum of the two bars 
    area = length * height 

    find the max area and return it 

    1. variable to keep track of max area a container can hold 
    2. two pointer to iterate through the height array and calculate the area 
    3. update the max area variable if a area greater than the max area variable is found 
    4. return max area variable 
    '''
    def maxArea(self, heights: List[int]) -> int:
        # variable keep track of container max area
        maxArea = 0

        # two pointer technique to find and calculate areas 
        left = 0
        right = len(heights) - 1

        while left < right:
            length = right - left
            height = min(heights[left], heights[right])
            area = length * height

            # update maxArea if area is greater than the current max
            maxArea = max(area, maxArea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea
