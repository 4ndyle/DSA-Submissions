"""
Input:
    - List[int] : numbers 
    - int : target 
Output:
    - [int, int] : [index1, index2] such that index1 + index2 = target
Constraints:
    - index1 < index2
    - exactly one valid solution
    - length of numbers: [2,30000]
    - range of values (numbers): [-1000,1000]
    - range of values (target): [-1000,1000]
Plan:
    1. Create two pointers (left and right) at the start and end of the array
    2. While left < right: 
        currentSum = numbers[left] + numbers[right]

        if currentSum < target, increment the left pointer
        if currentSum > target, decrement the right pointer 
        if currentSum == target, return [left+1,right+1]
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
                return [left+1, right+1]
        