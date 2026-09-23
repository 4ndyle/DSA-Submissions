"""
Input:
    - List[int] : numbers
    - int : target
Output:
    - List[int] : [index1, index2] such that nums[index1] + nums[index2] = target
Constraints:
    - numbers sorted in ascending order
    - exactly one valid solution
    - O(1) addtional space
    - index1 < index2
    - possible length of numbers: [2,30000]
    - possible values of numbers: [-1000,1000]
    - possible values of target: [-1000,1000]

Plan:
1. Create variables
    - left = 0
    - right = len(numbers) - 1
2. while left < right:
        currSum = numbers[left] + numbers[right]

        if currSum < target:
            increment left 
        elif currSum > target: 
            decrement right 
        else:
            return [left+1, right+1]        
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum < target: 
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    