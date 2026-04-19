class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        # two pointers 
        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]
        minHeight = min(leftMax, rightMax)

        totalWater = 0

        while left < right: 
            # if leftMax < rightMax, increment left pointer 
            if leftMax < rightMax:
                # calculate the amount of water for current left pointer
                if left != 0:
                    totalWater += minHeight - height[left]

                left += 1
                leftMax = max(leftMax, height[left])
            else:
                # calculate the amount of water for current left pointer
                if right != len(height) - 1:    
                    totalWater += minHeight - height[right]

                right -= 1
                rightMax = max(rightMax, height[right])

            minHeight = min(leftMax, rightMax)

        return totalWater