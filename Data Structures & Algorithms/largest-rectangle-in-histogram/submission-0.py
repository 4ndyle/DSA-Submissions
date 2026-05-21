class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            left = i 

            while stack and stack[-1][1] > heights[i]:
                # cant expand previous widths anymore
                poppedIndex, height = stack.pop()
                width = i - poppedIndex

                currArea = height * width
                maxArea = max(maxArea, currArea)

                left = poppedIndex

            stack.append((left, heights[i]))

        while stack:
            poppedIndex, height = stack.pop()   
            width = len(heights) - poppedIndex

            currArea = height * width
            maxArea = max(maxArea, currArea)
            
        # calculate the remaining heights in the stack , 
        return maxArea