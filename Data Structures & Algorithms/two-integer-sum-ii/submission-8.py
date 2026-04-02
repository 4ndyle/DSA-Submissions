"""
Input:
    - List[int] : numbers (sorted in ascending order)
    - int : target
Output:
    - List[int] : [index1, index2] such that they add up to a target and index1 < index2
Constraints:
    - range of values : -1000 <= numbers[i] <= 1000
    - length of numbers : 2 <= numbers.lenth <= 1000
    - -1000 <= target <= 1000

Plan: Create two pointers at the start and end of the list and move pointers based on whether
their current sum is less/equal/greater than the target
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create two pointers at the start and end of numbers list 
        left = 0
        right = len(numbers) - 1

        # move the pointers until we encounter a sum between numbers[left] and numbers[right] = target
        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                break
                
        return [left + 1, right + 1]
