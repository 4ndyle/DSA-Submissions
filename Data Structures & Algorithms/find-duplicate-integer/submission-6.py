"""
Input:
    - List[int] : nums
Output:
    - int : duplicate number in the list 
Constraints:
    - nums contains n + 1 integers 
    - each integer is in the range [1,n]
    - range of values: 1 <= n <= 10000
    - length of input list: length = n + 1

Plan:
We use each index in our array as a map to mark each element in that specific index. If the element in the specific index is already negative, we 
have already enncountered that number. 
index = currNum - 1

Examples:
nums = [1,2,3,2,2]

Iteration 0:
currNum = 1
index = 1 - 1 = 0
mark nums[0] as negative 
[-1,2,3,2,2]

Iteration 1:
currNum = 2
index = 2 - 1 = 1
mark nums[1] as negative 
[-1,-2,3,2,2]

Iteration 2:
currNum = 3
index = 3 - 1 = 2
mark nums[2] as negative 
[-1,-2,-3,2,2]

Iteration 3:
currNum = 2
index = 2 - 1 = 1
nums[1] is already negative, return 2
[-1,-2,-3,2,2]
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # calculate the index for the current number 
            numIndex = abs(num) - 1

            # if the number at numIndex is already negative, we have encounter the number already, return curr number
            if nums[numIndex] < 0:
                return abs(num)

            # mark the number at the index as negative 
            nums[numIndex] = -nums[numIndex]

        return -1




