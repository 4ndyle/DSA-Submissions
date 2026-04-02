class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create two pointers at start and end index 
        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            print(f"adding {numbers[left]} + {numbers[right]} = {currentSum}")

            # move left pointer if sum less than target 
            if currentSum < target: 
                left += 1
            # move right pointer if sum is greater than target
            if currentSum > target:
                right -= 1
                
            if currentSum == target:
                return [left+1, right+1]